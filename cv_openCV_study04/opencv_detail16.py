# ROI
# in computer vision : Region of Interest

import cv2

img = cv2.imread("hummingbird.jpg")
img = cv2.pyrDown(img)

roi = cv2.selectROI(img)
crop = img[int(roi[1]): int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])] # 이미지 크기

#print(roi)

cv2.imshow("image", crop)
cv2.waitKey(0)
cv2.destroyAllWindows()