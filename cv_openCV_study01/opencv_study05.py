import cv2
import numpy as np


img = cv2.imread("images/paper.jpg", 0)
edges1 = cv2.Canny(img, 30, 70)
edges2 = cv2.Canny(img, 50, 70)

display_image = np.hstack((img, edges1, edges2)) # np.vstack((img, edges1, edges2))

cv2.imshow("Edge Image", display_image)

cv2.waitKey(0)