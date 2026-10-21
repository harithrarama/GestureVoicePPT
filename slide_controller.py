
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

start_x = None
start_time = 0
last_swipe_time = 0

SWIPE_THRESHOLD = 0.18
SWIPE_WINDOW = 0.7
COOLDOWN = 1.0

print("GestureVoicePPT started!")
print("Open PowerPoint and press F5.")
print("Swipe LEFT: Next slide")
print("Swipe RIGHT: Previous slide")
print("Press Q in the camera window to quit.")

while cap.isOpened():
    success, frame = cap.read()

    if not success:
        print("Could not access webcam.")
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    message = "Show your hand"
    current_time = time.time()

    if results.multi_hand_landmarks:
        hand = results.multi_hand_landmarks[0]

        mp_draw.draw_landmarks(
            frame, hand, mp_hands.HAND_CONNECTIONS
        )

        wrist_x = hand.landmark[
            mp_hands.HandLandmark.WRIST
        ].x

        if start_x is None:
            start_x = wrist_x
            start_time = current_time
            message = "Tracking hand"

        else:
            movement = wrist_x - start_x
            elapsed = current_time - start_time

            if elapsed > SWIPE_WINDOW:
                # Restart tracking if the swipe took too long
                start_x = wrist_x
                start_time = current_time
                message = "Tracking hand"

            elif (
                abs(movement) >= SWIPE_THRESHOLD
                and current_time - last_swipe_time >= COOLDOWN
            ):
                if movement < 0:
                    message = "Next Slide"
                    pyautogui.press("right")
                    print("Swipe LEFT -> Next slide")
                else:
                    message = "Previous Slide"
                    pyautogui.press("left")
                    print("Swipe RIGHT -> Previous slide")

                last_swipe_time = current_time
                start_x = wrist_x
                start_time = current_time

            else:
                message = "Move hand to swipe"

    else:
        start_x = None

    cv2.putText(
        frame, message, (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX, 0.8,
        (0, 255, 0), 2
    )

    cv2.imshow("GestureVoicePPT", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
hands.close()
cv2.destroyAllWindows()
