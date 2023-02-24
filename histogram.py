import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

#histograms allow us to distribute pixel intensity distributions in an image
#histograms are kind of like graphs or plots

#grayscale histogram

img = cv.imread('catto_smol.jpg')
cv.imshow('Cat', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# # cv.imshow('Circle', circle) 

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# mask = cv.bitwise_and(img, i mg, mask=circle)
# cv.imshow('Mask', mask)

# #grayscale histogram
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

#colored histogram

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

plt.figure()
plt.title('Colored Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim(0,256)

plt.show()
cv.waitKey(0)