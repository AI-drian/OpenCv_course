import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype ='uint8')
#cv.imshow('Blank', blank)

#Paint image certain color
blank[100:300, 350:400] = 0, 0, 255
#cv.imshow('Red', blank) 

#Draw a rectangle
cv.rectangle(blank, (100,50), (200,200), (0,255,0), thickness = 2)
#cv.imshow('Rectangle', blank)


#Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[1]//2), 40, (0,0,255), thickness=2)
#cv.imshow('Circle', blank)

#Draw a line
cv.line(blank, (100,10), (200,200), (255,255,255), thickness = 1)
#cv.imshow('Line', blank)

#Write text on an image
cv.putText(blank, 'Hello', (225, 225), cv.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)
#cv.imshow('Text', blank)

cv.waitKey(0)