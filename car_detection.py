import cv2

# know we will load our classifier of car-- haarcascade which we have downloaded in the form of zip

car_classifier = cv2.CascadeClassifier('D:/ML projects/opencv/resources/cars.xml')

vid = cv2.VideoCapture('D:/ML projects/opencv/resources/traffic_1.mp4')

# to read tthe frame automitacally we will run a while loop
    
    
    
    
while True:
    ret, frame =vid.read()
    # this was read the image from the video which we have given to a variable vid.
    
    if ret == False:
        break
    # when any image not found from the frame it will break the loop and come out.
    
    # now we canvert image to gray scale image to make the processing fast
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # know to detect the car
    
    car = car_classifier.detectMultiScale(gray, 1.04985, 6)
    
    # the gray scale variables - gray in our case
    # scale factor = paramater to specifies how much the image size is reduce at each image scale
    # 6 is here minNeighbors
    
    # display the frame
    
    for (x, y, w, h) in car:
        cv2.rectangle(frame,(x, y), (x+w , y+h), (80, 80 , 255, 2))
    # here the syntax goes like this
#    frame thet image which it has read
#    x, y are the coordinates
#    x+w, y+h will make the rectangle
#    here is the width of formal rectangle

    # to display that image
    cv2.imshow('Car Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # when we press q statement will be close or wxit
vid.release()
cv2.destroyAllWindows()
    
    
    
    
    