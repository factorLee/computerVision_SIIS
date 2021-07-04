import cv2

img = cv2.imread("./images/paper.jpg", 0)

# IMREAD_FLAGS
# cv2.IMREAD_COLOR : 1 컬러 이미지로 불러오기
# cv2.IMREAD_GRAYSCALE : 0 grayscale로 이미지 불러오기
# cv2.IMREAD_UNCHANGED : -1 : alpha channel 유지하면서 이미지 불러오기


cv2.imshow("image", img)
key_value = cv2.waitKey(0) & 0xff

if key_value == 27:
    cv2.destroyAllWindows()
elif key_value == ord('s'): # ord() 아스키코드 값을 10진수로 반환
    cv2.imwrite("output_paper.png", img)