import cv2 as cv
import numpy as np


# reads image
img = cv.imread('samples/images/city_1.jpg')
# shows the resized image
cv.imshow('original_img', img)



# rescale an image 
def rescaleFrame(frame, scale=0.18):
  width = int(frame.shape[1] * scale)
  height = int(frame.shape[0] * scale)
  dimensions = (width, height)

  return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)



# translating an image
def translate(img, x, y):
  # generate translation matrix and img dimensions
  transMat = np.float32([[1, 0, x], [0, 1, y]])
  dimensions = (img.shape[1], img.shape[0])

  return cv.warpAffine(img, transMat, dimensions)



translated_img = translate(img, 100, 100)
cv.imshow('translated_img', translated_img)



# rotating an image
def rotate(img, angle, rotPoint=None):
  (height, width) = img.shape[:2]

  if rotPoint is None:
    # declaring the rotating point defaults
    rotPoint = (width// 2, height// 2)

  # generate rotation matrix and img dimensions
  rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
  dimensions = (width, height)


  return cv.warpAffine(img, rotMat, dimensions)



rotated = rotate(img, 45)
cv.imshow('rotated_img', rotated)



# flipping an image 
flipped_img = cv.flip(img, 1)
cv.imshow('flipped_img', flipped_img)



cv.waitKey(0)
