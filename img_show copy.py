import cv2
import sys

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('camera open failed')
    sys.exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) ==27:
        break


cap.release()
cv2.destroyAllWindows()


cv2.imshow('image',img)
cv2.waitKey()
