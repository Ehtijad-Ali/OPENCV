# convert the origional video into gray videos

import cv2

# capture the original video
cap = cv2.VideoCapture('resources/video_1.mp4')

while (cap.isOpened()):
    ret, frame =cap.read()

    # convert original video into gray video.
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # black and white image
    (thresh, binary)= cv2.threshold(grayframe, 127, 255, cv2.THRESH_BINARY)
    if ret == True:
        cv2.imshow('video', binary)
        if cv2.waitKey(1) &0xFF == ord('q'):
            break
    else:
         break
cap.release()
cv2.distroyAllWindows()