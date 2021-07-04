# 피라미드 기법 (pyramid)
# Level 0 : Original Size
# Level 1 : up의 경우 *2, down의 경우 1/2
# 피라미드 up의 경우
#   - 원래 이미지의 크기를 2배 늘린다.
#   - 이미지 샘플링을 크게 하고 blur 처리
# 피라미드 down의 경우
#   - 원래 이미지의 크기를 1/2로 줄인다.
#   - 이미지 샘플링을 작게 하고 blur 처리
# 피라미드 연산의 장점
#   1. 낮은 해상도(연산 처리 강점)
#   2. 다양한 이미지의 크기를 얻을 수 있다.
#   3. 쉽게 이미 처리를 얻을 수 있다.
#   4. edge를 쉽게 찾을 수 있다.


import cv2

img = cv2.imread("paper.jpg")
print(img.shape)

# img = cv2.pyrUp(img)
# print(img.shape)
# cv2.imshow("pyrUP1",img)
# img = cv2.pyrUp(img)
# print(img.shape)
# cv2.imshow("pyrUP2",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

img = cv2.pyrDown(img)
print(img.shape)
cv2.imshow("pyrDown1",img)
img = cv2.pyrDown(img)
print(img.shape)
cv2.imshow("pyrDown2",img)
cv2.waitKey(0)
cv2.destroyAllWindows()