#  resolution of  camera

import cv2
import numpy as np

cap =  cv2.VideoCapture(0)
#resolution
cap.set(3, 1280)
cap.set(4, 720)

def hd_resolution():
    cap.set(3, 1280)
    cap.set(4, 720)

hd_resolution()    

while(True):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('camera', frame)
        if cv2.waitKey(0) &0xFF == ord('q'):
            break
    else:
        break

    cap.release()
    cv2.distroyAllWindows()