import cv2
import numpy as np
import RPi.GPIO as GPIO
from control.led import led
from vision_system.face_detection import face_detection
from vision_system.set_camera import set_camera
from os.path import *

abs_path = dirname(abspath(__file__))
model_path = '/vision_system/models/haar.xml'
abs_model_path = abs_path+model_path

print(abs_model_path)

cap = set_camera()
classifier = face_detection(abs_model_path)

if __name__ == '__main__':

    try:

        while True:

            ret, frame = cap.read()
            frame, faces = classifier.detect_faces(frame)

            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'): break

    finally:
    
        cap.release()
        cv2.destroyAllWindows()
