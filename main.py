import cv2
import numpy as np
from modules.detection import *
import os

cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)

if __name__ == '__main__':

    try:

        while True:

            ret, frame = cap.read()

            avg_light = average_light(frame)
            
            frame = cv2.resize(frame, (320, 240 ))

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            face_cascade = cv2.CascadeClassifier('haar.xml')

            try:
                faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

                for (x, y, w, h) in faces:

                    cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
            finally:
                cv2.imshow('frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'): break

    finally:
    
        cap.release()
        cv2.destroyAllWindows()
