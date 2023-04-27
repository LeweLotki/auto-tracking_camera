import cv2
import numpy as np
import RPi.GPIO as GPIO
from control.led import led
from control.set_board import set_board 
from vision_system.face_detection import face_detection
from vision_system.set_camera import set_camera
from os.path import *

abs_path = dirname(abspath(__file__))
model_path = '/vision_system/models/haar.xml'
abs_model_path = abs_path+model_path

set_board()
cap = set_camera()
classifier = face_detection(abs_model_path)

led_32 = led(pin=32)

if __name__ == '__main__':

    try:

        while True:

            ret, frame = cap.read()
            frame, faces = classifier.detect_faces(frame)

            if faces != (): led_32.set_brightness(duty_cycle=100)
            else: led_32.set_brightness(duty_cycle=0)

            cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'): break

    finally:
    
        cap.release()
        cv2.destroyAllWindows()
