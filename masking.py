import cv2 as cv
import numpy as np

#masking is done by bitwise operators.
#masking allows us to focus on certain parts of an image

img = cv.imread('catto_smol.jpg')
cv.imshow('Cat', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow('Blank', blank)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# cv.imshow('Mask', mask)

#masked image
masked_image = cv.bitwise_and(img, img, mask=mask)
# cv.imshow('Masked image', masked_image)

#masked image but with a weird shape
rectangle = cv.rectangle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), (100,100), 255, -1)
circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
weird_shape = cv.bitwise_or(rectangle, circle)
weird_masked_image = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('Weird masked image', weird_masked_image)

cv.waitKey(0)