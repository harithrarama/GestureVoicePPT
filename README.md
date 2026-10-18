# GestureVoicePPT ✋🎙️

A Python-based project designed to control PowerPoint presentations using **hand gestures and voice commands**. It uses computer vision to detect hand movements and speech recognition to interpret voice commands for hands-free slide navigation.

## 🚀 Features

- **Hand Detection:** Detects hands in real time using a webcam.
- **Gesture Recognition:** Intended to navigate slides using hand movements.
- **Voice Control:** Recognizes voice commands for presentation navigation.
- **PowerPoint Integration:** Uses keyboard automation to control slides.
- **Real-Time Processing:** Uses OpenCV and MediaPipe for hand tracking.

## 🛠️ Technologies Used

- Python
- OpenCV
- MediaPipe
- PyAutoGUI
- SpeechRecognition
- PyAudio

## 📂 Project Structure

```text
GestureVoicePPT/
├── hand_detection.py
├── voice_control.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/harithrarama/GestureVoicePPT.git
cd GestureVoicePPT
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Running the Project

Start hand detection:

```bash
python hand_detection.py
```

Start voice control separately:

```bash
python voice_control.py
```

**Note:** These scripts currently run separately unless you combine them into a single controller.

## 🎮 Intended Controls

| Input | Action |
|---|---|
| Say "Next" | Next slide |
| Say "Previous" | Previous slide |
| Say "First" | First slide |
| Say "Last" | Last slide |
| Say "Start" | Start slideshow |
| Say "Stop" | Exit slideshow |
| Hand swipe right | Intended to move to the next slide |
| Hand swipe left | Intended to move to the previous slide |

## 📌 Requirements

- Python installed on your computer.
- A webcam for hand detection.
- A microphone for voice commands.
- Microsoft PowerPoint installed.
- Internet access for Google-based speech recognition.

Keep PowerPoint in slideshow mode when testing navigation commands. Keyboard automation sends commands to the active window, so ensure PowerPoint has focus.

## 🚧 Project Status

Hand detection using OpenCV and MediaPipe is implemented. Voice control and PowerPoint keyboard automation are being developed and tested. Reliable gesture-based navigation and combined gesture-and-voice control are still in progress.

## 👩‍💻 Author

**Harithra Rama**


