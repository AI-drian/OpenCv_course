import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

large = cv.imread('photos/dog.jpg')
img =cv.resize(large, (450,300))
cv.imshow('Dog', img)


#BGR to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR', hsv_bgr)

#BGR to L+a+b
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
cv.imshow('Lab', lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# #--Matplotlib
# plt.imshow(lab)
# plt.show()

# plt.imshow(rgb)
# plt.show()

cv.waitKey(0)