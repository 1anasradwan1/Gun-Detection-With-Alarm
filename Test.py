import numpy as np
import cv2
import imutils

gun_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
camera = cv2.VideoCapture(0)

first_frame = None

while True:
    ret, frame = camera.read()
    if not ret:
        print("Error: Could not read frame from camera.")
        break

    fram = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(fram, cv2.COLOR_BGR2GRAY)

    gun = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))

    gun_exists = False
    if len(gun) > 0:
        gun_exists = True
        for (x, y, w, h) in gun:
            fram = cv2.rectangle(fram, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = fram[y:y + h, x:x + w]

    if first_frame is None:
        first_frame = gray
        continue

    cv2.imshow("security", fram)
    key = cv2.waitKey(1) & 0xFF

    if gun_exists:
        print("Gun detected")
    else:
        print("Gun not detected")

    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
