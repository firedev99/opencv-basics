import cv2 as cv
import numpy as np


# read the image 
img = cv.imread('samples/images/goose_1.jpg')
# show the image 
cv.imshow('original_img', img)


# generates a canvas based on img
blank = np.zeros(img.shape[:2], dtype='uint8')


# generates a mask
mask = cv.circle(blank, (img.shape[1] // 2 + 60, img.shape[0] // 2 + 26), 175, 255, -1)
cv.imshow('mask', mask)



masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('mask_bitwise_and', masked)



cv.waitKey(0)