
<div align="center">

# Motion Sketch

**A real-time computer vision application that lets you draw in the air using hand gestures.**

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8.svg?style=flat&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-00A89D.svg?style=flat&logo=google&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243.svg?style=flat&logo=numpy&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

</div>

---

## Overview

**Motion Sketch** is an interactive virtual whiteboard powered by computer vision. By utilizing your webcam, the application tracks your hand movements in real-time and translates them into strokes on a digital canvas. 

Built with OpenCV and Google's MediaPipe, the application uses advanced landmark detection to understand the position of your fingers. It intelligently detects when your index finger is extended to draw, and stops drawing when your finger is bent, providing a seamless "air-writing" experience.

## Features

* **Real-Time Hand Tracking:** Utilizes MediaPipe's robust hand-tracking models for highly accurate, low-latency finger detection.
* **Gesture-Based Drawing:** Automatically detects drawing intent. Extend your index finger straight to write, and bend it slightly to lift the virtual "pen."
* **Dual-View Interface:** Displays both the live webcam feed (with skeletal landmark tracking) and a clean, standalone digital canvas window.
* **Quick Reset:** Instantly clear the canvas using keyboard bindings without restarting the application.

## 💻 Tech Stack

* **Language:** Python
* **Computer Vision:** OpenCV (`cv2`)
* **Machine Learning / Tracking:** MediaPipe (`mediapipe`)
* **Matrix Operations:** NumPy (`numpy`)

## 🚀 Installation & Setup

To run Motion Sketch on your local machine, follow these steps:

**1. Clone the repository**
```bash
git clone [https://github.com/yourusername/Motion-Sketch.git](https://github.com/yourusername/Motion-Sketch.git)
cd Motion-Sketch

```

**2. Create a virtual environment (Recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

```

**3. Install the required dependencies**

```bash
pip install opencv-python mediapipe numpy

```

**4. Run the application**

```bash
python app.py  # Replace app.py with your actual script name if different

```

## How to Use

Once the application launches, your webcam will turn on and two windows will appear.

### Gestures:

* **To Draw:** Hold up your index finger so that the tip is straight. Move your hand to draw on the black canvas in magenta (`#FF00FF`).
* **To Stop Drawing (Lift Pen):** Bend your index finger slightly (lowering the tip below the PIP joint). Moving your hand will no longer leave a trail.

### ⌨️ Keyboard Controls:

* Press **`r`** - **R**eset/Clear the entire canvas.
* Press **`q`** or **`Q`** - **Q**uit the application and close the webcam.

## 🤝 Collaboration & Contact

I am passionate about computer vision, interactive media, and building creative tech solutions. I am actively open to collaboration!

If you want to contribute—whether it's adding new colors, implementing multi-finger gestures (like zooming or erasing), or optimizing the tracking—feel free to fork the repo, submit a pull request, or reach out.

**Contact me:**

* **Email:** narayanprasadpattanayak2009@gmail.com
* **LinkedIn:** [LinkedIn]](https://www.linkedin.com/in/narayan-prasad-pattanayak-b40309367/)


## 📄 License

This project is licensed under the MIT License.
