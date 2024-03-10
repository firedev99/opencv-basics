import cv2 as cv
import matplotlib.pyplot as plt


# reads the original image
img = cv.imread('samples/images/butterfly_1.jpg')



# show the original img 
cv.imshow('original__img', img)



# converts the image into grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray_img', gray)



# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv_img', hsv)



# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lad_img', lab)



# BGR to RGBA
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb_img', rgb)



# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv_bgr_img', hsv_bgr)



plt.imshow(rgb)
plt.show()



cv.waitKey(0)