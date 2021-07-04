# bit 연산 : extraction(추출)
# - masking에 큰 도움
# - AND, OR, XOR, NOT를 사용한다.


import cv2

# img1, img2의 크기를 맞춰줘야함
img1 = cv2.imread("paper.jpg")
print(img1.shape)
img2 = cv2.imread("hummingbird.jpg")
img2 = cv2.resize(img2, (640, 426))
print(img2.shape)


# bit_and = cv2.bitwise_and(img1, img2) # and: eg. 빨간색은 빨간색끼로 모인다.

# bit_or = cv2.bitwise_or(img1, img2)

# bit_xor = cv2.bitwise_xor(img1, img2)

bit_not = cv2.bitwise_not(img2)

cv2.imshow("bit", bit_not)


cv2.waitKey(0)
cv2.destroyAllWindows()