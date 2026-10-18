
import cv2
import mediapipe as mp
import pyautogui
import time

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

cap = cv2.VideoCapture(0)

previous_x = None
last_swipe_time = 0
cooldown = 1.0
swipe_threshold = 0.15

print("GestureVoicePPT started!")
print("Open PowerPoint in Slide Show mode.")
print("Swipe LEFT: Next slide | Swipe RIGHT: Previous slide")
print("Press Q in the camera window to quit.")

while cap.isOpened():
    success, frame = cap.read()

    if not success:
        print("Could not access webcam")
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    message = "Show your hand"

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            wrist_x = hand_landmarks.landmark[
                mp_hands.HandLandmark.WRIST
            ].x

            current_time = time.time()

            if previous_x is not None:
                movement = wrist_x - previous_x

                if (
                    abs(movement) > swipe_threshold
                    and current_time - last_swipe_time > cooldown
                ):
                    if movement < 0:
                        message = "Next Slide"
                        pyautogui.press("right")
                    else:
                        message = "Previous Slide"
                        pyautogui.press("left")

                    last_swipe_time = current_time
                    previous_x = None
                else:
                    message = "Hand Detected"

            if previous_x is None:
                previous_x = wrist_x
            else:
                previous_x = wrist_x

    else:
        previous_x = None

    cv2.putText(
        frame,
        message,
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.imshow("GestureVoicePPT", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
hands.close()
cv2.destroyAllWindows()
