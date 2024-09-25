# import libraries
import cv2

# read the images from the directory
img = cv2.imread('resources/image.jpg')
img_1 = cv2.resize(img, (600, 600))

# show the image
cv2.imshow('image', img)
cv2.imshow('image', img_1)

# display the image
cv2.waitKey(0)
cv2.distroyAllWindows()
