import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width =  int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    capture.set(3, width)
    #we can access properties of the capture function through numbers. 3 means width, 4 height, 10 for brightness, etc.
    #so above we're basically setting the value of the 3rd property of capture to the width param we passed through the function.
    capture.set(4, height) 

capture = cv.VideoCapture(0)
while True:
    isTrue, frame =  capture.read()
    frame_resized = rescaleFrame(frame, 0.5)

    cv.imshow('Video Resized', frame_resized)

    if(cv.waitKey(20) & 0xFF==ord('d')):
        break

capture.release()
cv.destroyAllWindows()