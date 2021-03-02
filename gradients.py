import cv2 as cv
import numpy as np

img =cv.imread('photos/dog.jpg')
img =cv.resize(img, (400,250))
cv.imshow('Dog', img)

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('Gray', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel 
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined = cv.bitwise_or(sobelx, sobely)
cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined)

# Canny --Uses sobel in its calculations
canny = cv.Canny(gray, 150,175)
cv.imshow('Canny', canny)


cv.waitKey(0)