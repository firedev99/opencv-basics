import cv2 as cv



# reads the image
img = cv.imread('samples/images/city_1.jpg')


# rescale an image by defining a function 
def rescaleFrame(frame, scale=0.7):
  width = int(frame.shape[1] * scale)
  height = int(frame.shape[0] * scale)
  dimensions = (width, height)

  return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


resized_img = rescaleFrame(img)
# shows the image itself
cv.imshow('resized_img', resized_img)



# resize an image using built in function 
resized_cv = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('resized_img_cv', resized_cv)



# converting an image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray_img', gray)



# blur an image using gaussian blur
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('gaussian_blur_img', blur)



# edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('canny_edges', canny)



# reduced canny edges 
canny_reduced = cv.Canny(blur, 125, 175)
cv.imshow('canny_edges_reduced', canny_reduced)



# dilating reduced canny edges 
dilated = cv.dilate(canny_reduced, (7, 7), iterations=3)
cv.imshow('canny_edges_reduced_dilating', dilated)



# eroding dilated canny edges
eroded = cv.erode(dilated, (3, 3), iterations=1)
cv.imshow('eroded', eroded)



# cropping an image 
croped = img[50:400, 0:500]
cv.imshow('cropped_img', croped)




cv.waitKey(0)