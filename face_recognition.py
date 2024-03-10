import cv2 as cv


celebrities = ['Aaron Paul', 'Gal Gadot', 'Johnny Depp', 'Scarlett Johansson', 'SRK']

haar_cascade = cv.CascadeClassifier('classifiers/haarcascade_frontalface_default.xml')



# create the face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer.create()
# read the face recognizer model
face_recognizer.read('model/face_trained.yml')



img = cv.imread(r"E:\ML\stock assets\celebrities\Scarlett Johansson\01edc26576c398678651f73f437fe4e1.jpg")
# img = cv.imread(r"E:\ML\stock assets\celebrities\SRK\d3b8f995ffd359d080f383677be19583.jpg")


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray__img', gray)


faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)


for (x, y, w, h) in faces_rect:
  faces_roi = gray[y:y+h, x:x+h]

  label = face_recognizer.predict(faces_roi)

  cv.putText(img, str(celebrities[label]), (25, 50), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), 2)
  cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)




cv.imshow('detected_face', img)


cv.waitKey(0)