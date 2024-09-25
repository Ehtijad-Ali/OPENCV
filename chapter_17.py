# joining two images

import cv2
import numpy as np

img =  cv2.imread('resources/plane.jpg')
img_1 = cv2.resize(img,(500,500))

image = cv2.imread('resources/animal.jpg')
image_2 = cv2.resize(image,(500,500))


join = np.hstack((img_1, image_2))


cv2.imshow('joined image', join)

cv2.waitKey(0)
cv2.distroyAllWindows()

