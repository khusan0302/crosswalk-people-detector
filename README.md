# 🛑 Crosswalk Detection and Traffic Signal Assistance System

A real-time crosswalk detection system that recognizes both pedestrians and vehicles using YOLOv8, and provides visual safety feedback based on simulated traffic light logic.

---

## 📽 Demo

<div align="center">
  <img src="demo_original.gif" width="45%" alt="Original CCTV">
  <img src="demo_result.gif" width="45%" alt="Detection Result">
  <p><i>Left: Original input footage | Right: System output with annotations</i></p>
</div>

---

## 📌 Project Overview

This system simulates an urban crosswalk equipped with traffic signals and computer vision. It performs:

- Pedestrian and vehicle detection via YOLOv8 (`yolov8m.pt`)
- Traffic signal simulation (automatic RED/GREEN switching)
- On-screen annotations like `CROSS! (person)` or `STOP (car)` based on safety context
- Result video export and ESC-key termination
- Fully modular design: `main.py`, `detector.py`, `drawing.py`, `traffic_signal.py`

---

## 📂 Project Structure

.
├── main.py
├── src/
│ ├── detector.py
│ ├── drawing.py
│ └── traffic_signal.py
├── models/
│ └── yolov8m.pt
├── data/
│ ├── crosswalk_cctv.mp4
│ └── result.mp4
├── demo_original.gif
├── demo_result.gif
├── LICENSE
└── README.md


---

## 🚀 How to Run

1. Install dependencies:

```bash
pip install ultralytics opencv-python pillow

Place crosswalk_cctv.mp4 in data/ and yolov8m.pt in models/.

Run the system:

bash
python main.py
Press ESC to exit. The result will be saved as data/result.mp4.

🧠 Key Features
✅ YOLOv8 detection for both pedestrians and vehicles

✅ Safety feedback: "CROSS!" / "DANGER!" / "STOP" / "GO"

✅ English font rendering, no font file dependencies

✅ Lightweight, modular, maintainable

🔗 Reference
Inspired by DMU Computer Vision – CrossWalk CCTV, but fully refactored with modular structure, new logic, and improved annotations.
ChatGPT 4o

📜 License
This project is licensed under the MIT License.
