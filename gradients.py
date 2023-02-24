import cv2 as cv
import numpy as np

#think of gradients as edges from a programming perspective only
#alternatives to find edges other than canny

img = cv.imread('catto_smol.jpg')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# laplacian

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# sobel (calculates gradients in x and y)

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)

sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

# cv.imshow('SobelX', sobelx)

# cv.imshow('SobelY', sobely)

combined_sobel = cv.bitwise_or(sobelx, sobely)
cv.imshow('Combined Sobel', combined_sobel)

# canny

canny = cv.Canny(gray, 150, 175)

# cv.imshow('Canny', canny)

cv.waitKey(0)