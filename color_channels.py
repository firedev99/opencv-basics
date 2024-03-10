import cv2 as cv
import numpy as np


# read the image 
img = cv.imread('samples/images/butterfly_1.jpg')
# show the image 
cv.imshow('original_img', img)
# generate a blank page
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank__canvas', blank)


# split the color channels 
b, g, r = cv.split(img)


# merge the color channels for specific channel
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])


# show the channels
cv.imshow('blue_channel', b)
cv.imshow('green_channel', g)
cv.imshow('red_channel', r)



# show the channels
cv.imshow('blue_channel_2', blue)
cv.imshow('green__channel_2', green)
cv.imshow('red_channel_2', red)



print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)



# merged channels
merged = cv.merge([b, g, r])
cv.imshow('merged__img', merged)




cv.waitKey(0)