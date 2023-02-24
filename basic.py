import cv2 as cv

img = cv.imread('catto_smol.jpg')
cv.imshow("Cat", img)

#convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Cat', gray)

#blur (remove noise to decrease artifacts due to bad lighting)
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

#edge cascade (finding edges in images)
canny = cv.Canny(img, 125, 175)
#cv.imshow('Canny', canny)

#you can pass in blurred images to Canny to reduce the amount of edges detected

#dilating the image (finding details based on structure)
dilated = cv.dilate(canny, (3,3), iterations=1)
#cv.imshow('Dilated', dilated)

#eroding (removing dilation to get back original structure)
erode = cv.erode(dilated, (3,3), iterations=1)
#cv.imshow('Erode', erode)

#resize
resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
#cv.imshow('Resize', resize)

#cropping
crop = img[50:200, 200:400]
cv.imshow('Cropped', crop)

cv.waitKey(0)