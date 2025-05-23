import cv2
import time
from src.detector import detect_and_annotate_people
from src.traffic_signal import get_traffic_light_status
from src.drawing import draw_boundary_lines, draw_text

# Video processing
cap = cv2.VideoCapture("data/crosswalk_cctv.mp4")
start_time = time.time()

# Set up video writer to save output in data folder
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
out = cv2.VideoWriter("data/result.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    current_time = int(time.time() - start_time)
    signal = get_traffic_light_status(current_time, 4, 7)
    left_line, right_line = draw_boundary_lines(frame, signal)

    # Draw traffic signal status
    if signal == "RED":
        frame = draw_text(frame, "RED LIGHT", (50, 50), font_size=25, color=(0, 0, 255))
    else:
        frame = draw_text(frame, "GREEN LIGHT", (50, 50), font_size=25, color=(0, 255, 0))

    # Run person detection and annotations
    frame = detect_and_annotate_people(frame, signal, left_line, right_line)

    cv2.imshow("Crosswalk Assistance", frame)
    out.write(frame)  # Save each frame to the output file

    if cv2.waitKey(1) & 0xFF == 27: # ESC key to exit
        break

cap.release()
out.release()
cv2.destroyAllWindows()