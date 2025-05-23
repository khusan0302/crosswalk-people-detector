import cv2
from ultralytics import YOLO
from src.drawing import draw_text

model = YOLO("models/yolov8m.pt")

# COCO class ids: 0 = person, 2 = car, 3 = motorcycle, 5 = bus, 7 = truck
vehicle_ids = [2, 3, 5, 7]

def detect_and_annotate_people_and_vehicles(frame, signal, left_line, right_line):
    results = model.predict(frame)
    COCO_NAMES = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat']  # truncated for brevity
    for box in results[0].boxes:
        cls = int(box.cls[0])
        label_name = COCO_NAMES[cls] if cls < len(COCO_NAMES) else f'class {cls}'
        cls = int(box.cls[0])
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        center_x = (x1 + x2) // 2

        if cls == 0:  # person
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            if left_line[1] < center_x < right_line[1]:
                if signal == "GREEN":
                    frame = draw_text(frame, f"CROSS! ({label_name})", (x1, y1 - 50), font_size=25, color=(0, 255, 0))
                    frame = draw_text(frame, "CROSS!", (x1, y1 - 50), font_size=25, color=(0, 255, 0))
                else:
                    frame = draw_text(frame, f"DANGER! ({label_name})", (x1, y1 - 50), font_size=25, color=(0, 0, 255))

        elif cls in vehicle_ids:  # vehicle
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 0), 2)
            label = "STOP" if signal == "GREEN" else "GO"
            color = (0, 0, 255) if signal == "GREEN" else (0, 255, 0)
            frame = draw_text(frame, f"{label} ({label_name})", (x1, y1 - 40), font_size=25, color=color)

    return frame
