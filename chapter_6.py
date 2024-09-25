# load the videos

import cv2

cap = cv2.VideoCapture('resources/video_1.mp4')

while (cap.isOpened()):
    ret, frame =cap.read()
    if ret == True:
        cv2.imshow('video', frame)
        if cv2.waitKey(1) &0xFF == ord('q'):
            break
    else:
         break
cap.release()
cv2.distroyAllWindows()

