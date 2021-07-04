# image filtering
# 이미지에 존재하는 픽셀에 해당하는 픽셀의 주위에 있는 픽셀들을 활용한 특정한 함수를 적용한 결과를 기반으로 수정하는 개념

# 1. mask를 생성
# 2. 이 mask를 기준으로 주변값들을 연산

# cv2.blur() 함수
# cv2.blur(image, destination, 커널의 사이즈, [achor type, border type])


import cv2

img = cv2.imread('paper.jpg')

img_blur = cv2.blur(img, (3,3))

cv2.imshow("original image", img)
cv2.imshow("blurred image", img_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()