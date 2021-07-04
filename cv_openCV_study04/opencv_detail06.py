# image translation : 옮김
# 이미지의 객체나 이미지 위치를 옮기는데 사용
# 옮기는 방향은 (x, y) 방향이다. -> 옮겨진 장소 (tx, ty)
# 
# transformation matrix M = [[1, 0, tx], [0, 1, ty]]

import cv2
import numpy as np

img = cv2.imread("hummingbird.jpg")
img = cv2.pyrDown(img)
height, width, _ = img.shape
# print(height, width)

flt_var = np.float32([[1, 0, 100], [0, 1, 50]]) # 32비트의 크기를 가진 실수
# print(flt_var)

img_trans = cv2.warpAffine(img, flt_var, (width, height))

cv2.imshow("original", img)
cv2.imshow("translated Image", img_trans)
cv2.waitKey(0)
cv2.destroyAllWindows()
