import cv2
import numpy as np

class face_detection:

    def __init__(self, abs_model_path : str):
        
        self.face_cascade = cv2.CascadeClassifier(abs_model_path)


    def detect_faces(self, frame : np.ndarray):

            frame = cv2.resize(frame, (320, 240))
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            try:
                faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
                for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

                return frame, faces

            except Exception as e: print(e)

