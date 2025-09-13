A gesture-controlled Volume Controller built with Python, OpenCV, MediaPipe, and Pycaw. Adjust system volume by moving your thumb and index finger: pinch to lower, spread to raise. Features real-time hand tracking, smooth volume mapping, and a live on-screen volume bar with percentage display.

# 🔊 Gesture Volume Control (Python + OpenCV + MediaPipe + Pycaw)

Control your system’s volume with just your hand ✋  
This project uses **MediaPipe** for hand tracking and **Pycaw** for controlling system audio.

---

## 📝 Description
The project detects your **thumb** and **index finger** using MediaPipe Hands and maps their distance to the system’s audio level. Moving your fingers apart increases the volume, while bringing them closer decreases it. A **volume bar and percentage display** provide real-time feedback.

---

## 🚀 Features
- **Hand Tracking** → detects thumb & index tips in real-time  
- **Volume Control** → pinch = lower volume, spread = higher volume  
- **Visual Feedback** → live volume bar and percentage display  
- **Smooth Control** → natural and intuitive gesture-based interaction  

---

## 🛠️ Tech Stack
- [Python](https://www.python.org/)  
- [OpenCV](https://opencv.org/)  
- [MediaPipe](https://developers.google.com/mediapipe)  
- [Pycaw](https://github.com/AndreMiras/pycaw)  

---

## 📦 Installation
```bash
# Clone the repo
git clone https://github.com/YOUR-USERNAME/gesture-volume-control.git
cd gesture-volume-control

# Install dependencies
pip install -r requirements.txt
