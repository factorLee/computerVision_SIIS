# image rotation = rotation transformation 
# 이미지의 축을 변경 (회전)
# 변경할 각도를 지정해줘야 한다.
# transformation matrix M = [[cos, -sin], [sin, cos]]
# OpenCV에서는 scaled rotation이라고 한다.

import cv2

img = cv2.imread("hummingbird.jpg")
img = cv2.pyrDown(img)
height, width, _ = img.shape

# 너비에서반, 높이에서 반 = 가운데 값이다.
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1) # 회전할때 기준 위치, 각도 등을 지정

img_rotation = cv2.warpAffine(img, rotation_matrix, (width, height))

cv2.imshow("original", img)
cv2.imshow("Rotated Image", img_rotation)
cv2.waitKey(0)
cv2.destroyAllWindows()

