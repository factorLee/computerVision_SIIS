import cv2

cap = cv2.VideoCapture(0)

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
cap.set(3, 320) # flag 값이 3이라고 정해져 있음
cap.set(4, 240)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True:
        # gray = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2GRAY)
        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()