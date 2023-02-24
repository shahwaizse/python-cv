# color spaces
import cv2 as cv

img = cv.imread('catto_smol.jpg')

cv.imshow('Cat', img)

#BGR to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

#BGR TO HSV (hue saturation value, based on how humans conceive color)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

#BGR TO L*A*B
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('Lab', lab)

#BGR TO RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('rgb', rgb)

cv.waitKey(0)