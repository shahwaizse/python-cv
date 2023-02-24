import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
#cv.imshow('Blank', blank)

#blank[200:300, 300:400] = 255,0,0
#cv.imshow('Green', blank)

#cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED)
#cv.imshow('Rectangle', blank)

#cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,255,0), thickness=3)
#cv.imshow('Circle', blank)

#cv.line(blank, (0,0), (300,300), (255,0,0), 2)
#cv.imshow('Line', blank)

#img = cv.imread('catto_smol.jpg')
#cv.imshow('Cat', img)

cv.putText(blank, 'Hello', (200,255), cv.FONT_HERSHEY_TRIPLEX, 1, (255,0,0), 1)
cv.imshow('Text', blank)

cv.waitKey(0)