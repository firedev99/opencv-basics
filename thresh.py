import cv2 as cv


# read the image 
img = cv.imread('samples/images/kitten_1.jpg')
# show the image 
cv.imshow('original_img', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray_img', img)



# simple thresholding 
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('thresh', thresh)



# simple thresholding (inversed)
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('thresh_inversed', thresh_inv)



# adaptive thresholding mean 
adaptive_mean_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('adaptive_mean_thresh', adaptive_mean_thresh)


# adaptive thresholding gaussian
adaptive_gaussian_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('adaptive_gaussian_thresh', adaptive_gaussian_thresh)



cv.waitKey(0)