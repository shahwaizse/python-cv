import cv2 as cv

#thresholding is binarizing of an image, to make pixels either black or white
#each pixel gets compared to thresholded value, if less then its black, if greater then pixel will be white

img = cv.imread('catto_smol.jpg')
cv.imshow('Cat', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
# cv.imshow('Simple Threshold', thresh)

threshold, thresh_inverse = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
# cv.imshow('Simple Threshold Inverse', thresh_inverse)

#adaptive thresholding

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 5)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)