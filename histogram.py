import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('photos/magica.png')
#img =cv.resize(img, (450,300))
cv.imshow('Magica', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
#cv.imshow('Gray', gray)

#Masking image, only for fun...
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 2, -1)
mask = cv.bitwise_and(gray, gray, mask=circle)
#cv.imshow('Mask', mask)

#GrayScale histogram
gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])
plt.figure('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
#plt.show()

#Color Histogram
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim(0,256)
plt.show()

cv.waitKey(0)

#OpenCV Course - Full Tutorial with Python 2:15:20 Thresholding