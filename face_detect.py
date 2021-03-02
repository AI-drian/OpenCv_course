import cv2 as cv

img = cv.imread('photos/promoe.jpg')
img = cv.resize(img, (500,400))
cv.imshow('Promoe', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray People', gray)

haar_cascade =cv.CascadeClassifier('haar_face.xml')

#Min_neighbours höj/sänk om den hittar för många/få ansikten!
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f'Number of faces: {len(faces_rect)} ')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0,255,0), thickness=1)

cv.imshow('Detected Faces', img)


cv.waitKey(0)

#OpenCV Course - Full Tutorial with Python 2:50:20