#  how to change the prespective of an image

import numpy as np
import cv2

img = cv2.imread('resources/warp.jpg')
img_1 =cv2.resize(img,(800,800))
print(img_1.shape)

# defining points

point1 = np.float32([[60, 55], [40,400],[300, 20], [200,33]])
width = 800
height = 800

point2 =np.float32([[0, 0], [800, 0], [0, height],[width, height]])
matrix = cv2.getPerspectiveTransform(point1, point2)

out_img = cv2.warpPerspective(img_1, matrix, (width, height))

cv2.imshow('origional', img_1)
cv2.imshow('transform', out_img)
cv2.waitKey(0)
cv2.distroyAllWindows()