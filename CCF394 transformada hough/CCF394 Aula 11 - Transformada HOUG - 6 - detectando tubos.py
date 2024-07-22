import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

# load the image, clone it for output, and then convert it to grayscale
image = cv2.imread(args["image"])
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#detect circles in the image
#circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, param1=40,minRadius=10,maxRadius=35)
circles = cv2.HoughCircles(gray,
                           cv2.HOUGH_GRADIENT,
                           minDist=6,
                           dp=1.1,
                           param1=150,
                           param2=15,
                           minRadius=6,
                           maxRadius=10)
#print(len(circles[0][0]))
# ensure at least some circles were found
if circles is not None:
    # convert the (x, y) coordinates and radius of the circles to integers
    circles = np.round(circles[0, :]).astype("int")
    # count = count+1   

    # print(count) 

    # loop over the (x, y) coordinates and radius of the circles
    for (x, y, r) in circles:
        # draw the circle in the output image, then draw a rectangle
        # corresponding to the center of the circle
        cv2.circle(output, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

    # show the output image
   # cv2.imshow("output", np.hstack([output]))
    cv2.imwrite('output.jpg',np.hstack([output]),[cv2.IMWRITE_JPEG_QUALITY, 70])
    cv2.imshow("teste",output)
    cv2.waitKey(0)

import cv2

image = cv2.imread('tubos.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,27,3)

cnts = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
count = 0
for c in cnts:
    area = cv2.contourArea(c)
    x,y,w,h = cv2.boundingRect(c)
    ratio = w/h
    ((x, y), r) = cv2.minEnclosingCircle(c)
    if ratio > .85 and ratio < 1.20 and area > 50 and area < 120 and r < 7:
        cv2.circle(image, (int(x), int(y)), int(r), (36, 255, 12), -1)
        count += 1

print('Count: {}'.format(count))

cv2.imshow('thresh', thresh)
cv2.imshow('image', image)
cv2.waitKey()



'''
import cv2
import matplotlib.pyplot as plt
import numpy as np
#pre processing
img = cv2.imread('a2MTm.jpg')
blur_hor = cv2.filter2D(img[:, :, 0], cv2.CV_32F, kernel=np.ones((11,1,1), np.float32)/11.0, borderType=cv2.BORDER_CONSTANT)
blur_vert = cv2.filter2D(img[:, :, 0], cv2.CV_32F, kernel=np.ones((1,11,1), np.float32)/11.0, borderType=cv2.BORDER_CONSTANT)
mask = ((img[:,:,0]>blur_hor*1.2) | (img[:,:,0]>blur_vert*1.2)).astype(np.uint8)*255

plt.imshow(mask)

ou


circles = cv2.HoughCircles(mask,
                           cv2.HOUGH_GRADIENT,
                           minDist=8,
                           dp=1,
                           param1=150,
                           param2=12,
                           minRadius=4,
                           maxRadius=10)
output = img.copy()
for (x, y, r) in circles[0, :, :]:
  cv2.circle(output, (x, y), r, (0, 255, 0), 4)


'''
