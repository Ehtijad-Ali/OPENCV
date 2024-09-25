# saving video in the computer

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

# Video writer object and file output, codec, writing format
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Corrected function name
out = cv2.VideoWriter('resources/new_video.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width, frame_height))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # Write grayscale frame to new video
        out.write(frame)
        
        # Display grayscale frame
        cv2.imshow('video', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
         break

# Release resources and close windows
cap.release()
out.release()
cv2.destroyAllWindows()