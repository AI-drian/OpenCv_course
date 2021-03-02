import cv2 as cv
import numpy as np

img = cv.imread('photos/magica.png')
cv.imshow('Magica', img)

def translate(img, x, y):
    '''
    -x  ----> Left
    +x  ----> Right
    -y  ----> Up
    +y  ----> Down
    '''
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions =(img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

def rotate(img, angle ,rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) 
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


#Translation
translate = translate(img, -100, 100)
#cv.imshow('Translate', translate)

#Rotation
rotaded = rotate(img, 45)
#cv.imshow('Rotaded', rotaded)

#Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
#cv.imshow('Resized', resized)

#Flipping img
flip = cv.flip(img, 0)
#cv.imshow('Flip', flip)

cropped = img[200:400, 150:250]
#cv.imshow('Cropped', cropped)

cv.waitKey(0)