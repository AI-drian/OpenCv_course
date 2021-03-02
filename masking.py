import cv2 as cv
import numpy as np

img = cv.imread('photos/dog.jpg')
img =cv.resize(img, (450,300))
cv.imshow('Dog', img)

#img.shape has to be the same size as img!
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank image', blank)

mask = cv.circle(blank, (img.shape[1]//2 + 120, img.shape[0]//2 -30), 100, 255, -1)
cv.imshow('Mask', mask)

masked =cv.bitwise_and(img, img,mask=mask)
cv.imshow('Masked image', masked)


cv.waitKey(0)