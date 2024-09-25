# face detection 

import cv2

cascade_face = cv2.CascadeClassifier('resources/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret , img = cap.read()
    print(ret)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face =  cascade_face.detectMultiScale(gray, 1.3, 5)


    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 4)
        cv2.imshow('image', img)
        k = cv2.waitKey(30)& 0xFF 
        if k ==  True:
            break
