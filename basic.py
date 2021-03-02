import cv2 as cv

img = cv.imread('photos/magica.png')

cv.imshow('Magica', img)

#Convert img to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

#Blur img
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
#cv.imshow('Blur', blur)

#Edge Cascade (Prova stoppa in t.ex. blur istället för img)
canny = cv.Canny(img, 125, 175)
#cv.imshow('Canny', canny)

#Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
#cv.imshow('Dilated', dilated)

#Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
#cv.imshow('Erode', eroded)

#Resize
resized =cv.resize(img, (500,500))
#cv.imshow('Resize', resized)

#Cropping
cropped = img[25:150, 40:200]
#cv.imshow('Crop', cropped)

cv.waitKey(0)