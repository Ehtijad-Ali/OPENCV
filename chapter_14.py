import numpy as np
import cv2

# draw canvas

img = np.zeros((600,600))
img_1 = np.ones((600,600))


# adding color to the canvas
# color channels to the canvas
colored_img = np.zeros((600,600, 3), np.uint8)
# color complete image
colored_img[:] = 255,0, 255 

colored_img[100:100, 100:100] = 2, 0, 500


#cv2.imshow('blaked', img)
#cv2.imshow('white', img_1)
cv2.imshow('colored_image', colored_img)



cv2.waitKey(0)
cv2.distroyAllWindows()




