import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

def draw_boundary_lines(frame, signal):
    h, w = frame.shape[:2]
    left_x = int(w * 0.5) - 100
    right_x = int(w * 0.5)
    tan_l, tan_r = np.tan(np.radians(-50)), np.tan(np.radians(50))

    lx1, ly1, lx2, ly2 = left_x, 0, int(left_x + tan_l * h), h
    rx1, ry1, rx2, ry2 = right_x, 0, int(right_x + tan_r * h), h
    color = (0, 0, 255) if signal == "RED" else (0, 255, 0)

    cv2.line(frame, (lx1, ly1), (lx2, ly2), color, 3)
    cv2.line(frame, (rx1, ry1), (rx2, ry2), color, 3)
    return (lx1, lx2), (rx1, rx2)

def draw_text(img, text, pos, font_size=50, color=(255, 255, 255), font_name="arial.ttf"):
    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_pil)
    try:
        font = ImageFont.truetype(font_name, font_size)
    except:
        font = ImageFont.load_default()
    draw.text(pos, text, font=font, fill=(color[2], color[1], color[0]))
    return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
