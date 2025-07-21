# 🔫 Real-Time Gun Detection with Alarm System

A Python-based real-time surveillance application that uses OpenCV to detect firearms through a webcam feed and triggers an alarm sound when a gun is detected. This project demonstrates the practical use of computer vision for safety and threat detection systems.

---

## 🚀 Features

- 📷 Real-time video surveillance using webcam
- 🎯 Gun detection using Haar Cascade XML classifier
- 🔊 Audible alarm system powered by `pygame`
- ⚡ Efficient and responsive using multithreaded alarm playback
- ✅ Lightweight and easy to integrate into other projects

---

## 🧠 How It Works

1. Captures live video feed from the default camera.
2. Converts each frame to grayscale for detection.
3. Uses a Haar Cascade model (`cascade.xml`) to detect firearms.
4. When a gun is detected:
   - A green bounding box and label are shown on screen.
   - An alarm sound is triggered to alert the user.

---

## 📦 Requirements

- Python 3.8 – 3.11 recommended (⚠️ Not tested on 3.13+)
- OpenCV
- imutils
- pygame

### 🔧 Install Dependencies
```bash
pip install opencv-python imutils pygame
