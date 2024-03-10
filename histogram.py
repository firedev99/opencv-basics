import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt



# read the image 
img = cv.imread('samples/images/butterfly_1.jpg')
# show the image 
cv.imshow('original_img', img)



# convert image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray_img', gray)



# generates a blank canvas 
blank = np.zeros(img.shape[:2], dtype='uint8')

# generate a circle 
circle = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)


# mask the circle into the image
masked = cv.bitwise_and(gray, gray, mask = circle) 
cv.imshow('masked__img', masked)



# grayscale histogram
gray_hist = cv.calcHist([gray], [0], masked, [256], [0, 256])


plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('bins')
plt.ylabel('px')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()






# bgr histogram
plt.figure()
plt.title('BGR Histogram')
plt.xlabel('bins')
plt.ylabel('px')
colors = ('b', 'g', 'r')

for i, channel in enumerate(colors):
  bgr_hist = cv.calcHist([img], [i], None, [256], [0, 256])
  plt.plot(bgr_hist, color=channel)
  plt.xlim([0, 256])

plt.show()



cv.waitKey(0)