# basic function or manpulation in opencv
import numpy as np
import cv2
img = cv2.imread('resources/horses.jpg')

# resize the image
img_1 = cv2.resize(img, (400, 400))

# convert origional image into gray image
gray_image = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)

# black and white image
(thresh, binary)= cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# convert origional image into blurred image 
blurr_image = cv2.GaussianBlur(img_1,(35, 35), 0 )

# edge detection
edge_image = cv2.Canny(img_1, 48, 43)

# thickness of line
dilated_image = cv2.dilate(edge_image, (7, 7), iterations= 1)

# make thinner outline
ero_image = cv2.erode(dilated_image, (7, 7), iterations= 1)


cv2.imshow('resize', img_1) 
cv2.imshow('gray_image', gray_image)
cv2.imshow('black_white' ,binary)
cv2.imshow('blurr_image', blurr_image)
cv2.imshow('edge_detection', edge_image)
cv2.imshow('dilated_image', dilated_image)
cv2.imshow('erosion', ero_image)



cv2.waitKey(0)
cv2.distroyAllWindows()
   

