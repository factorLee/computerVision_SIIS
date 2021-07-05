import numpy as np
import cv2

cap = cv2.VideoCapture("slow_traffic_small.mp4")

roi = (300, 200, 100, 50)

while(1):
    ret, img = cap.read()
    #roi : Region Of Interest; 관심영역
    roi = img[200:250, 300:400]

    if ret == True:

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

        cv2.imshow("traffic video", img)

        key_value = cv2.waitKey(1) & 0xFF
        if key_value == 27: # esc
            break
    else:
        break