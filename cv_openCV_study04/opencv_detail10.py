import cv2
import numpy as np

img = cv2.imread("hummingbird.jpg")
img = cv2.pyrDown(img)
height, width, _ = img.shape

mat1 = np.float32([[100, 600], [200, 500], [300, 230], [500, 400]])
mat2 = np.float32([[200, 200], [300, 250], [400, 0], [600, 500]])
