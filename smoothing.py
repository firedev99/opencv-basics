import cv2 as cv




# read the image 
img = cv.imread('samples/images/goose_2.jpg')
# show the image 
cv.imshow('original__img', img)



# averaging 
average = cv.blur(img, (7, 7))
cv.imshow('average__img', average)



# gaussian blur
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('gaussian__blur__img', gauss)



# median blur
median = cv.medianBlur(img, 7)
cv.imshow('median__blur__img', median)



# bilateral blur
bilateral = cv.bilateralFilter(img, 25, 50, 50)
cv.imshow('bilateral__blur__img', bilateral)



cv.waitKey(0)