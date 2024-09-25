# import libraries
import numpy as np
import cv2
from cv2 import imwrite
from cv2 import imshow

# load the image

img = cv2.imread('resources/image.jpg')

# resize the image
img = cv2.resize(img, (500, 500))

# convert the origional image into gray image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# black and white image
(thresh, binary)= cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)


cv2.imwrite('image_gray.jpg', gray)
cv2.imwrite('image_bw.jpg', binary)

# display image forever
cv2.waitKey(0)
cv2.destroyAllWindows()