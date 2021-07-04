# pillow에서의 크롭
import cv2

img1 = cv2.imread("./images/paper.jpg")
img2 = cv2.imread("./images/color.jpg")

print(img1.shape)
print(img2.shape)
# textoftheimage = img[109:331, 94:475]
# img[99:321, 84:465] = textoftheimage

img1 = cv2.resize(img1, (640, 420))
img2 = cv2.resize(img2, (640, 420))

# added_img = cv2.add(img1, img2)
added_img = cv2.addWeighted(img1, 0.8, img2, 0.2, 0)
cv2.imshow("image", added_img)
cv2.waitKey(0)
cv2.destoryAllwindow()