import cv2 as cv

#for capturing images
img = cv.imread('catto_smol.jpg')
cv.imshow('Cat', img)

#for capturing videos
capture = cv.VideoCapture(0)

while True:
    isTrue, frame =  capture.read()
    cv.imshow('Video', frame)

    if(cv.waitKey(20) & 0xFF==ord('d')):
        break

capture.release()
cv.destroyAllWindows()

#cv.waitKey(0)