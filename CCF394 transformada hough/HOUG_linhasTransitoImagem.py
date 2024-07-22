'''

Hough Line Transformation
Finds lines in a binary image using the standard Hough transform.

The function implements the standard or standard multi-scale Hough transform
algorithm for line detection. See http://homepages.inf.ed.ac.uk/rbf/HIPR2/hough.htm for a good explanation of Hough transform.

Parameters
image	8-bit, single-channel binary source image. The image may be modified by the function.
lines	Output vector of lines. Each line is represented by a 2 or 3 element vector (ρ,θ) or (ρ,θ,votes) . ρ is the distance from the coordinate origin (0,0) (top-left corner of the image). θ is the line rotation angle in radians ( 0∼vertical line,π/2∼horizontal line ). votes is the value of accumulator.
rho	Distance resolution of the accumulator in pixels.
theta	Angle resolution of the accumulator in radians.
threshold	Accumulator threshold parameter. Only those lines are returned that get enough votes ( >threshold ).
srn	For the multi-scale Hough transform, it is a divisor for the distance resolution rho . The coarse accumulator distance resolution is rho and the accurate accumulator resolution is rho/srn . If both srn=0 and stn=0 , the classical Hough transform is used. Otherwise, both these parameters should be positive.
stn	For the multi-scale Hough transform, it is a divisor for the distance resolution theta.
min_theta	For standard and multi-scale Hough transform, minimum angle to check for lines. Must fall between 0 and max_theta.
max_theta	For standard and multi-scale Hough transform, maximum angle to check for lines. Must fall between min_theta and CV_PI.

___________________________________________________
 The Probabilistic Hough Line Transform

A more efficient implementation of the Hough Line Transform. It gives as output the extremes of the detected lines (x0,y0,x1,y1)
In OpenCV it is implemented with the function HoughLinesP()

lines	=cv.HoughLinesP(image, rho, theta, threshold[, lines[, minLineLength[, maxLineGap]]]	)

Parameters
image	8-bit, single-channel binary source image. The image may be modified by the function.
lines	Output vector of lines. Each line is represented by a 4-element vector (x1,y1,x2,y2) , where (x1,y1) and (x2,y2) are the ending points of each detected line segment.
rho	Distance resolution of the accumulator in pixels.
theta	Angle resolution of the accumulator in radians.
threshold	Accumulator threshold parameter. Only those lines are returned that get enough votes ( >threshold ).
minLineLength	Minimum line length. Line segments shorter than that are rejected.
maxLineGap	Maximum allowed gap between points on the same line to link them.



'''


import cv2
import numpy as np
img = cv2.imread("lines.png")
cv2.imshow("Imagem Original", img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 75, 150)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 30, maxLineGap=250)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
cv2.imshow("Edges", edges)
cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
