import cv2
import numpy as np

# Function to handle trackbar changes
def nothing(x):
    pass

img = cv2.imread('resources/plane.jpg')
img_1 = cv2.resize(img, (800, 600))

# Convert image to HSV
hsv_img = cv2.cvtColor(img_1, cv2.COLOR_BGR2HSV)

# Create a window for trackbars
cv2.namedWindow("bars")
cv2.resizeWindow("bars", 640, 300)

# Create trackbars for color selection
cv2.createTrackbar('Hue min', 'bars', 0, 179, nothing)
cv2.createTrackbar('Hue max', 'bars', 179, 179, nothing)
cv2.createTrackbar('Saturation min', 'bars', 0, 255, nothing)
cv2.createTrackbar('Saturation max', 'bars', 255, 255, nothing)
cv2.createTrackbar('Value min', 'bars', 0, 255, nothing)
cv2.createTrackbar('Value max', 'bars', 255, 255, nothing)

while True:
    # Get current positions of all trackbars
    hue_min = cv2.getTrackbarPos('Hue min', 'bars')
    hue_max = cv2.getTrackbarPos('Hue max', 'bars')
    sat_min = cv2.getTrackbarPos('Saturation min', 'bars')
    sat_max = cv2.getTrackbarPos('Saturation max', 'bars')
    val_min = cv2.getTrackbarPos('Value min', 'bars')
    val_max = cv2.getTrackbarPos('Value max', 'bars')

    # Create a mask based on the current trackbar settings
    lower_bound = np.array([hue_min, sat_min, val_min])
    upper_bound = np.array([hue_max, sat_max, val_max])
    mask = cv2.inRange(hsv_img, lower_bound, upper_bound)

    # Apply the mask to the original image
    masked_img = cv2.bitwise_and(img_1, img_1, mask=mask)

    # Display the masked image
    cv2.imshow('masked image', masked_img)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
