# negative transformation
# 이미지의 반대를 찾는 변환
# 밝은 것을 어두운 것으로, 어두운 것을 밝은 것으로
# color 채널과 관련이 많이 있다.

import cv2

img = cv2.imread("hummingbird.jpg")
img = cv2.pyrDown(img)
img_neg = 1 - img


cv2.imshow("Oirginal", img)
cv2.imshow("negative", img_neg)
cv2.waitKey(0)
cv2.destroyAllWindows()