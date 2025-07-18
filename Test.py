import numpy as np
import cv2
import imutils

# Load cascade
gun_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
if gun_cascade.empty():
    print("Error: Cascade file not loaded properly.")
    exit()

# Start webcam
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Error: Camera could not be opened.")
    exit()

while True:
    ret, frame = camera.read()
    if not ret:
        print("Error: Could not read frame from camera.")
        break

    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect guns
    guns = gun_cascade.detectMultiScale(gray, 1.3, 5, minSize=(100, 100))

    gun_exists = False
    for (x, y, w, h) in guns:
        gun_exists = True
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, 'Gun Detected', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Security Feed", frame)

    if gun_exists:
        print("Gun detected")
    else:
        print("Gun not detected")

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
