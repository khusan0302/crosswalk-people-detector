import cv2
import time
from src.detector import detect_and_annotate_people
from src.traffic_signal import get_traffic_light_status
from src.drawing import draw_boundary_lines, draw_text_korean

# Video processing
cap = cv2.VideoCapture("data/crosswalk_cctv.mp4")
start_time = time.time()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    current_time = int(time.time() - start_time)
    signal = get_traffic_light_status(current_time, 4, 7)
    left_line, right_line = draw_boundary_lines(frame, signal)

    # Draw traffic signal status
    if signal == "RED":
        frame = draw_text_korean(frame, "빨간불", (50, 50), font_size=50, color=(0, 0, 255))
    else:
        frame = draw_text_korean(frame, "초록불", (50, 50), font_size=50, color=(0, 255, 0))

    # Run person detection and annotations
    frame = detect_and_annotate_people(frame, signal, left_line, right_line)

    cv2.imshow("Crosswalk Assistance", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
