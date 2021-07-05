import cv2
import time
import numpy as np

body_calssifier = cv2.CascadeClassifier("haarcascade_fullbody.xml")

cap = cv2.VideoCapture("walking.avi")

while cap.isOpened():
    time.sleep(0.05)

    ret, frame = cap.read()

    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        

        cars = body_calssifier.detectMultiScale(gray, 1.4, 2)

        for (x,y,w,h) in cars:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 255), 2)
            cv2.imshow("pedestrians", frame)

        if cv2.waitKey(1) & 0xFF == 'q':
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
