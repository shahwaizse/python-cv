#splitting and merging color channels
#color channels are red, green and blue
import cv2 as cv
import numpy as np
img = cv.imread('catto_smol.jpg')

blank = np.zeros(img.shape[:2], dtype='uint8')

# cv.imshow('Cat', img)

b, g, r = cv.split(img)

# cv.imshow('Blue', b)
# cv.imshow('REd', r)
# cv.imshow('Green', g)

print(img.shape)
print(b.shape)
print(r.shape)
print(g.shape)

#cv.split depicts grayscale images, in which higher concentration of colorway will be brighter, and vice versa 
#(the sky will be bright in b)

#visual colors instead of grayscale
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('REd', red)

#merging all the color channels back into one BGR image
merge = cv.merge([b,g,r])
cv.imshow('Merged', merge)

cv.waitKey(0)
