import sys
import cv2 as cv
import numpy as np
import easyocr
src = cv.imread('placas.png', cv.IMREAD_COLOR)
largura_desejada =800 
height, width, depth = src.shape
imgScale = largura_desejada/width
newX,newY = src.shape[1]*imgScale, src.shape[0]*imgScale
src = cv.resize(src,(int(newX),int(newY)))
src2=src.copy()
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 5)
rows = gray.shape[0]
circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8,
                           param1=100, param2=30,
                           minRadius=10, maxRadius=50)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])
        # centro
        cv.circle(src, center, 1, (20, 100, 255), 2)
        radius = i[2]
        cv.circle(src, center, radius, (255, 0, 0), 2)
        print(center)
cv.imshow("Original", src2)
cv.imshow("Saida", src)
cv.waitKey(0)
cv.destroyAllWindows()
x=src[int(center[1]-radius):int(center[1]+radius),int(center[0]-radius):int(center[0]+radius)]
cv.imshow("t",x)

reader = easyocr.Reader(['en'])
all_reads = reader.readtext(x)
print(all_reads)
