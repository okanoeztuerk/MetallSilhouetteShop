import sys
import cv2
import numpy as np
import svgwrite

def generate_svg_from_image_bytes(image_bytes):
    np_arr = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(np_arr, cv2.IMREAD_GRAYSCALE)

    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    edged = cv2.Canny(blurred, 50, 150)

    contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    h, w = image.shape
    dwg = svgwrite.Drawing(size=(f"{w}px", f"{h}px"))

    for contour in contours:
        path_data = "M " + " L ".join(f"{pt[0][0]},{pt[0][1]}" for pt in contour) + " Z"
        dwg.add(dwg.path(d=path_data, fill="black"))

    return dwg.tostring()
