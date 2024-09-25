import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
     
     # convert origional video into gray video
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    # black and white image
    (thresh, binary)= cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY)


    cv2.imshow('origional capture', frame)
    cv2.imshow('gray_capture', gray_frame)
    cv2.imshow('black_white', binary)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        break
    else:
        break

    cap.release()
    cv2.distroyAllWindows()

    