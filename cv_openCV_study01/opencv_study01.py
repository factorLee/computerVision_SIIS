import cv2

image = cv2.imread("images/color.jpg")

print(image.shape) # 세로 길이부터시작

cv2.imshow("Image show", image)
cv2.waitKey(3) # 0은 무기한 대기를 의미, 나머지 숫자는 기다리는 초*1000 (단위가 ms)