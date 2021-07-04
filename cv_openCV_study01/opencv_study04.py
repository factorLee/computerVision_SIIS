# erosion and dilation

import cv2
import numpy as np


img = cv2.imread("images/paper.jpg", 0)
kernel = np.ones((5,5), np.uint8)
ret, thresh = cv2.threshold(img, 175, 255, cv2.THRESH_BINARY)
erosion = cv2.erode(thresh, kernel)
dilation = cv2.dilate(thresh, kernel)



# edges1 = cv2.Canny(img, 30, 70)
# edges2 = cv2.Canny(img, 50, 70)

display_image = np.hstack((thresh, erosion, dilation)) # np.vstack((img, edges1, edges2))




cv2.imshow("Erosion &Dilation1", display_image)
cv2.waitKey(0)

edges = cv2.Canny(img, 30, 70)
erosion = cv2.erode(edges, kernel)
dilation = cv2.dilate(edges, kernel)
display_image = np.hstack((edges, erosion, dilation)) # np.vstack((img, edges1, edges2))

cv2.imshow("Erosion &Dilation2", display_image)
cv2.waitKey(0)