import cv2
import numpy as np


img = cv2.imread("images/gray.jpg", 0)
ret, thresh = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)


cv2.imshow("Gray Image", img)
cv2.imshow("Threashold", thresh)

cv2.waitKey(0)