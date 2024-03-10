import os 
import cv2 as cv 
import numpy as np

celebrities = ['Aaron Paul', 'Gal Gadot', 'Johnny Depp', 'Scarlett Johansson', 'SRK']
DIR = r'E:\ML\stock assets\celebrities'

haar_cascade = cv.CascadeClassifier('classifiers/haarcascade_frontalface_default.xml')


features = []
labels = []


def create_train():
  for person in celebrities:
    path = os.path.join(DIR, person)
    label = celebrities.index(person)

    for img in os.listdir(path):
      img_path = os.path.join(path, img)

      img_array = cv.imread(img_path)
      gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

      faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

      for (x, y, w, h) in faces_rect:
        faces_roi = gray[y:y+h, x:x+w]
        features.append(faces_roi)
        labels.append(label)



create_train()
print('Training Done!')


# create the face recognizer 
face_recognizer = cv.face.LBPHFaceRecognizer.create()


# generate numpy arrays 
features = np.array(features, dtype='object')
labels = np.array(labels)


# train the recognizer 
face_recognizer.train(features, labels)


# save the files
face_recognizer.save('model/face_trained.yml')
np.save('model/features.npy', features)
np.save('model/labels.npy', labels)