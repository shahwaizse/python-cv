import cv2 as cv
import numpy as np

img = cv.imread('catto_smol.jpg')

cv.imshow('Cat', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#cv.imshow('grey', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

#v.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)

#cv.imshow('Canny', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
#the threshold method basically binarizes an image, if intensity of a pixel is below 125, its set to black, and if > 125, its set to white
cv.imshow('Thresh', thresh)

#we can pass findContours either canny, or thresh
countours, hierarchies = cv.findContours(thresh , cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
#above method looks at the image, and returns two values
#contours: a python list of the co-ordinates of the contours in the image
#hierarchies: a hierachical list of the contours in the image (circles within a square, etc)
#RETR_EXTERNAL only returns external contours
#RETR_TREE returns hierachical contours
#RETR_LIST returns all the contours
#last param of findContours is the approximation method of the contours, CHAIN_APPROX_SIMPLE compresses the contours into simple ones

print(f'{len(countours)} these many contours found.')

cv.drawContours(blank, countours, -1, (0,0,255), 1)
cv.imshow('Contours drawn', blank)

cv.waitKey(0)