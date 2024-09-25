#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2

# Load the car classifier (Haar cascade)
car_classifier = cv2.CascadeClassifier(r'D:/ML projects/opencv/resources/cars.xml')

# Open the video file
vid = cv2.VideoCapture(r'D:/ML projects/opencv/resources/traffic_1.mp4')

# Check if the video loaded successfully
if not vid.isOpened():
    print("Error loading video.")
else:
    print("Video loaded successfully.")

    total_car_count = 0  # Initialize total car count

    while True:
        ret, frame = vid.read()  # Read a frame from the video

        if not ret:  # If no frame is returned, break the loop
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect cars in the frame
        cars = car_classifier.detectMultiScale(gray, scaleFactor=1.04985, minNeighbors=6)

        # Draw rectangles around detected cars and count them
        car_count = 0  # Initialize car count for the current frame
        for (x, y, w, h) in cars:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (80, 80, 255), 2)
            car_count += 1

        total_car_count += car_count  # Update total car count

        # Display the frame with detections
        cv2.putText(frame, f'Cars in frame: {car_count}', (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, f'Total cars: {total_car_count}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.imshow('Car Detection', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close all OpenCV windows
    vid.release()
    cv2.destroyAllWindows()


# In[ ]:




