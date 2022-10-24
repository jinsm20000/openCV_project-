import sys
import cv2
from cv2 import approxPolyDP
import numpy as np


src = cv2.imread('2.png')

if src is None:
    print('image load failed')
    sys.exit()

src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

th,src_bin = cv2.threshold(src_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

print(th)

contours, _ = cv2.findContours(src_bin,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

for pts in contours:
    if cv2.contourArea(pts) < 1000:
        continue

    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts,True)*0.02, True)
    if len(approx) != 4:
        continue
    w, h = 900, 500
    srcQuad = np.array([[approx[0, 0, :]],[approx[1, 0, :]],[approx[2, 0, :]],[approx[3, 0, :]]]).astype(np.float32)
    
    dstQuad = np.array([[w,h],[w,0],[0,0],[0,h]]).astype(np.float32)
    pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
    dst = cv2.warpPerspective(src, pers,(w,h))

    cv2.polylines(src, pts, True, (0,0,225))

cv2.imshow('src',src)
cv2.imshow('src_gray',src_gray)
cv2.imshow('src_gray',src_bin)
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()
