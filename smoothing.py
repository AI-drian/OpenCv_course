import cv2 as cv

img = cv.imread('photos/dog.jpg')
img =cv.resize(img, (450,300))
cv.imshow('Dog', img)

#Averaging Blur
average = cv.blur(img, (3,3))
cv.imshow('Average', average)

#Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian', gauss) 

#Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median', median)

#Bilateral Blur
bilateral = cv.bilateralFilter(img, 5, 45, 35) 
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)