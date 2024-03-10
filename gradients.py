import cv2 as cv
import numpy as np



# read the image 
img = cv.imread('samples/images/nature_1.jpg')
# show the image 
cv.imshow('original__img', img)



# convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray_img', gray)



# laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian', lap)



# sobel
sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobel_x, sobel_y)



# canny 
canny = cv.Canny(gray, 150, 175)



cv.imshow('sobel__x', sobel_x)
cv.imshow('sobel__y', sobel_y)
cv.imshow('sobel__combined', combined_sobel)
cv.imshow('canny__img', canny)



cv.waitKey(0)