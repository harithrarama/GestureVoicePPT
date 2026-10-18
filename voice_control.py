
import speech_recognition as sr
import pyautogui

recognizer = sr.Recognizer()

def voice_control():
    with sr.Microphone() as source:
        print("Listening... Say a command!")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
            command = recognizer.recognize_google(audio).lower()

            print("You said:", command)

            if "next" in command:
                pyautogui.press("right")
                print("Next slide")

            elif "previous" in command or "back" in command:
                pyautogui.press("left")
                print("Previous slide")

            elif "first" in command:
                pyautogui.press("home")
                print("First slide")

            elif "last" in command:
                pyautogui.press("end")
                print("Last slide")

            elif "start" in command:
                pyautogui.press("f5")
                print("Starting slideshow")

            elif "stop" in command or "exit" in command:
                pyautogui.press("esc")
                print("Ending slideshow")

            else:
                print("Command not recognized")

        except sr.WaitTimeoutError:
            print("No speech detected")

        except sr.UnknownValueError:
            print("Could not understand the voice")

        except sr.RequestError:
            print("Speech recognition service unavailable")

if __name__ == "__main__":
    while True:
        voice_control()
