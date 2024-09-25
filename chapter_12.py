import cv2
import numpy as np

# capture video
cap = cv2.VideoCapture(0)

# 10 is the key to set brightness
cap.set(10, 50) 

# 3 is the key to set width
cap.set(3, 600)

# 4 is the key to set height
cap.set(4, 400)

while(True):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('video', frame)
        if cv2.waitKey(1) &0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.distroyAllWindows()