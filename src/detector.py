import cv2
from ultralytics import YOLO
from src.drawing import draw_text

model = YOLO("models/yolo11n.pt")

def detect_and_annotate_people(frame, signal, left_line, right_line):
    results = model.predict(frame)
    for box in results[0].boxes:
        cls = int(box.cls[0])
        if cls == 0:  # person
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            center_x = (x1 + x2) // 2

            if left_line[1] < center_x < right_line[1]:
                if signal == "GREEN":
                    frame = draw_text(frame, "CROSS!", (x1, y1 - 50), font_size=25, color=(0, 255, 0))
                else:
                    frame = draw_text(frame, "DANGER!", (x1, y1 - 50), font_size=25, color=(0, 0, 255))
    return frame