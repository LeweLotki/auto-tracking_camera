import cv2
import numpy as np

def set_camera():

    cap = cv2.VideoCapture(0)

    cap.set(3, 640)
    cap.set(4, 480)

    return cap
