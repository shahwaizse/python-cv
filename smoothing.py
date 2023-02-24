import cv2 as cv

img = cv.imread('catto_smol.jpg')

cv.imshow('Cat', img)

#averaging (the pixel intensity of the center pixel will be set based on the intensities of the surrounding pixels)
#the kernel window will slide across the image, starting at 0,0 and ending at endpixel,endpixel
#btw this is why the kernel window can only be odd, because if it was even then there wouldn't be a center pixel

average = cv.blur(img, (7,7))
# cv.imshow('Average', average)

#gaussianblur (surrounding pixels are given weights, and the products of those weights determine the intensity of center)
#using this, there's less blur than averaging, bur it's more natural
#it uses sigmaX, which is the standard deviation in the x direction

gauss = cv.GaussianBlur(img, (7,7), 0)
# cv.imshow('Gaussian blur', gauss)

#medianblur (instad of average of surrounding pixels, it uses median of surrounding pixels. more effective than avg)
median = cv.medianBlur(img, 3)
# cv.imshow('Median', median)

#bilateral blurring (applies blurring, but retains the edges of the image. most effective blur, used in advanced projects)
bilateral = cv.bilateralFilter(img, 10, 35, 25)
#the second parameter is the diameter of the kernel
#the sigma space parameter in above function dictates how far away a pixel can influence the kernel process going on
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)