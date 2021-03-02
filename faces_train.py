import os
import cv2 as cv
import numpy as np

#people= ['Arnie', 'Bianca', 'Greta', 'Keanu', 'Oprah', 'Pew', 'Pope']

#List of names on folders
people = []
for i in os.listdir(r'C:\Users\adria\Desktop\Skola\kod\Python\openCv\faces'):
    p.append(i)
print(p)    

DIR = r'C:\Users\adria\Desktop\Skola\kod\Python\openCv\faces'

haar_cascade =cv.CascadeClassifier('haar_face.xml')

features = []
labels = []


def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1,
            minNeighbors=4)

            for(x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print('Training Complete--------')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recogizer = cv.face.LBPHFaceRecognizer_create()

#Train recognizer on features & labels list
face_recogizer.train(features, labels)

face_recogizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)

