# how to captuer web camera in  python

# import libraries
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# read until the end

while cap.isOpened():
    #capture frane by frame
    ret, frame = cap.read()

    # display frame
    if ret == True:
        cv2.imshow('frame', frame)
        
    # to quit with q key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
         break

# Release resources and close windows
cap.release()
cv2.destroyAllWindows()


