import cv2
import numpy as np

def find_coord(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Left clicked on the mouse button
        print("Coordinates (x, y):", x, y)

    # For color finding 
    if event == cv2.EVENT_RBUTTONDOWN:
        # Right clicked on the mouse button
        print("Coordinates (x, y):", x, y)

        # Get the BGR pixel values at the clicked coordinates
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]

        # Display the BGR values in the console
        print("BGR values:", b, g, r)

        # Display the BGR values on the image
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, f'BGR: {b}, {g}, {r}', (x, y), font, 1, (255, 0, 0), 2)

        # Show the updated image
        cv2.imshow('image', img)

if __name__ == '__main__':
    # Read an image
    img = cv2.imread('resources/warp.jpg', 1)
    img_1 =cv2.resize(img,(800, 800))

    # Display the original image
    cv2.imshow('image', img_1)

    # Set mouse callback function
    cv2.setMouseCallback('image', find_coord)

    # Wait for any key to be pressed
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
