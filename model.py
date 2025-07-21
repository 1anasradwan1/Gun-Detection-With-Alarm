import cv2
import imutils
import pygame
import threading

pygame.mixer.init()
alarm_sound = pygame.mixer.Sound("alarm.wav")  

gun_cascade = cv2.CascadeClassifier('cascade.xml')
if gun_cascade.empty():
    print("Error: Cascade file not loaded properly.")
    exit()

camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Error: Camera could not be opened.")
    exit()

alarm_playing = False

def play_alarm():
    global alarm_playing
    alarm_playing = True
    alarm_sound.play()
    pygame.time.wait(3000)  
    alarm_playing = False

while True:
    ret, frame = camera.read()
    if not ret:
        print("Error: Could not read frame from camera.")
        break

    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    guns = gun_cascade.detectMultiScale(gray, 1.6, 15, minSize=(100, 100))
    gun_exists = False

    for (x, y, w, h) in guns:
        gun_exists = True
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, 'Gun Detected', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    if gun_exists:
        print("Gun detected")
        if not alarm_playing:
            threading.Thread(target=play_alarm, daemon=True).start()
    else:
        print("Gun not detected")

    cv2.imshow("Security Feed", frame)

    if cv2.waitKey(1) == 27:  # ESC key
        break

camera.release()
cv2.destroyAllWindows()

