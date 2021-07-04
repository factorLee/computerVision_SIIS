import cv2

img = cv2.imread("images/paper.jpg")
img2 = cv2.imread("images/color.jpg")

print(img.shape)
print(img.size)
# 817, 920 = width * height * channel (640 *426 * 3)
print(img.dtype)

b, g, r = cv2.split(img)
b2,g2,r2 = cv2.split(img2)
img = cv2.merge((g2,b2,r2))

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
