import cv2 as cv


img_1 = cv.imread("samples/images/face_2.jpg")
img_2 = cv.imread("samples/images/group_1.jpg")
img_3 = cv.imread("samples/images/group_3.jpg")



# convert image to grayscale
gray_1 = cv.cvtColor(img_1, cv.COLOR_BGR2GRAY)
gray_2 = cv.cvtColor(img_2, cv.COLOR_BGR2GRAY)
gray_3 = cv.cvtColor(img_3, cv.COLOR_BGR2GRAY)


haar_cascade = cv.CascadeClassifier('classifiers/haarcascade_frontalface_default.xml')


faces_rect_1 = haar_cascade.detectMultiScale(gray_1, scaleFactor=1.1, minNeighbors=3)
faces_rect_2 = haar_cascade.detectMultiScale(gray_2, scaleFactor=1.1, minNeighbors=6)
faces_rect_3 = haar_cascade.detectMultiScale(gray_3, scaleFactor=1.1, minNeighbors=8)

# print(f'Number of faces found: {len(faces_rect)}')



for (x, y, w, h) in faces_rect_1:
  cv.rectangle(img_1, (x, y), (x + w, y + h), (0, 255, 0), 2)

for (x, y, w, h) in faces_rect_2:
  cv.rectangle(img_2, (x, y), (x + w, y + h), (0, 255, 0), 2)

for (x, y, w, h) in faces_rect_3:
  cv.rectangle(img_3, (x, y), (x + w, y + h), (0, 255, 0), 2)



cv.imshow('detected_face_1', img_1)
cv.imshow('detected_face_2', img_2)
cv.imshow('detected_face_3', img_3)



cv.waitKey(0)