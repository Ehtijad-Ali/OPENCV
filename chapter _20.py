# spiliting a videos into frames

import cv2

# capture the original video
cap = cv2.VideoCapture('resources/geeen_tea.mp4')

framenum = 0

while True:
    success, frame = cap.read()
    if success:
        cv2.imwrite(f'resources/frame/frame_{framenum}.jpg', frame)
    else:
        break

    framenum += 1

cap.release()

