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
                if faces != ():
                    (x, y) = self.__get_face_position(faces)
                    return {'x' : x, 'y' : y}
                return {}
            except Exception as e: print(e)

    def __get_face_position(self, faces):

        (x,y,w,h) = faces[0]
        x += (w / 2) - 160
        y += (h / 2) - 120

        return x, y
