import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectanglge', rectangle)

cv.imshow('Circle', circle)

#bitwise AND --> intersecting regions

bitwise_AND = cv.bitwise_and(rectangle, circle)

#cv.imshow('bitiwseAND', bitwise_AND)

#bitwise OR --> non-intersecting regions and intersecting regions

bitwise_OR = cv.bitwise_or(rectangle, circle)

#cv.imshow('bitwiseOR', bitwise_OR)

#bitwise NOT --> returns inverse of image

#bitwise_NOT = cv.bitwise_not(rectangle)

#cv.imshow('bitwiseNOT', bitwise_NOT)

bitwise_NOT = cv.bitwise_not(circle)

cv.imshow('bitwiseNOT', bitwise_NOT)

#bitwise XOR -->non-intersecting regions

bitwise_XOR = cv.bitwise_xor(rectangle, circle)

cv.imshow('bitwiseXOR', bitwise_XOR)

cv.waitKey(0)