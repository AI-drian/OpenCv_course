import numpy as np
import cv2 as cv

haar_cascade =cv.CascadeClassifier('haar_face.xml')

people= ['Arnold Swarchnegger', 'Bianca Ingrosso', 'Greta Thunberg', 'Keanu Reeves', 'Oprah Winfrey', 'Pewdipie', 'The Pope']
# features = np.load('features.npy')
# labels = np.load('labels.npy')

face_recogizer = cv.face.LBPHFaceRecognizer_create()
face_recogizer.read('face_trained.yml')

img = cv.imread(r'C:\Users\adria\Desktop\Skola\kod\Python\openCv\faces\faces_validation\who2.jpg')
img =cv.resize(img, (450,300))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

#Detect the Face
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]

    label, confidence = face_recogizer.predict(faces_roi)
    print(f'Label = {people[label]} with a conficence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness= 1)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness = 2)

cv.imshow('Detected face', img)

cv.waitKey(0)
