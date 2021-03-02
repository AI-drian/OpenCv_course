import cv2 as cv

img =cv.imread('photos/dog.jpg')
img =cv.resize(img, (400,250))
cv.imshow('Dog', img)

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('Gray', gray)

#Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Thresholded Simple', thresh)

#Simle thersholding Inversed
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Thresholded Simple-Inverse', thresh_inv)

#Adaptive Thresholding
adaptive_thres = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Threshold', adaptive_thres)

#Adaptive Thresholding Inversed
adaptive_thres_inv = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
cv.imshow('Adaptive Threshold-Inversed', adaptive_thres_inv)
cv.waitKey(0)