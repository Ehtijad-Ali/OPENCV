# import libraries
import numpy as np
import cv2

# load the image

img = cv2.imread('resources/image.jpg')

# resize the image
img = cv2.resize(img, (400, 400))

# convert the origional image into gray image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# show the gray image
cv2.imshow('gray', gray)

# show origional and gray image 
cv2.imshow('image', img)
cv2.imshow('gray image', gray)

# display image forever
cv2.waitKey(0)
cv2.destroyAllWindows()