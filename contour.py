import cv2 as cv
import numpy as np



# read the original image
img = cv.imread('samples/images/kitten_2.jpg')
# generate a shape
blank = np.zeros(img.shape, dtype="uint8")



# convert the image to grayscale
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
# cv.imshow('gray_img', gray)



# blur the image
# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
# cv.imshow('blur_img', blur)



# canny edges 
# canny = cv.Canny(blur, 125, 175)
# cv.imshow('canny_edges_img', canny)



ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# show the thresh image
cv.imshow('threshed_img', thresh)



contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')



# draw contours to blank canvas
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('contours_img', blank)



cv.waitKey(0)