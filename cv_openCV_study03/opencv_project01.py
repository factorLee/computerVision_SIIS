import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def faceDetector(img):
    # 그레이톤이 처리할량이 적어짐(색을 원하는게 아니라 디텍션이 목적이기 때문)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) # 임계치 지정

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

    return img

input_image = cv2.imread("./images/son.jpeg")
output_image = faceDetector(input_image)
cv2.imshow("face_test",output_image)

cv2.waitKey(0)
cv2.destroyAllWindows()