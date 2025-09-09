# ai-virtual-volume-control
A Python project that uses hand gestures to control your system volume in real time. The system leverages OpenCV for webcam input, MediaPipe for hand tracking, and PyCaw for controlling system audio.  When you bring your thumb and index finger closer or farther apart, the system adjusts the volume accordingly — just like a virtual volume knob.

# 🎚️ AI Virtual Volume Control  

Control your system volume with **hand gestures** using Python, OpenCV, MediaPipe, and PyCaw.  
This project turns your webcam into a **virtual volume knob**, where the distance between your **thumb and index finger** controls the audio level.  

---

## 📸 Demo  
👉 (Add a GIF or screenshot of your project running here)  

---

## 🚀 Features  
- Real-time **hand tracking** using MediaPipe.  
- Control **system volume** without touching your keyboard/mouse.  
- Smooth volume transition with distance-based mapping.  
- On-screen **volume bar & percentage display**.  

---

## 🛠️ Requirements  
Make sure you have Python 3.7+ installed, then install the required libraries:  

```bash
pip install opencv-python mediapipe comtypes pycaw numpy
