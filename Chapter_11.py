import cv2
import numpy as np

# Capture the original video
cap = cv2.VideoCapture(0)

# Video writer object and file output, codec, writing format
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Corrected function name
out = cv2.VideoWriter('resources/new_video.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width, frame_height), isColor=False)

while (cap.isOpened()):
    ret, frame = cap.read()

    # Convert original video into grayscale
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

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
