import cv2 as cv
import numpy as np


# blank canvas
blank = np.zeros((500, 500, 3), dtype='uint8')
blank_border_square = np.zeros((500, 500, 3), dtype='uint8')
blank_filled_square = np.zeros((500, 500, 3), dtype='uint8')
blank_line = np.zeros((500, 500, 3), dtype='uint8')
blank_text = np.zeros((500, 500, 3), dtype='uint8')
blank_circle = np.zeros((500, 500, 3), dtype='uint8')



# shows the blank canvas itself
cv.imshow('blank_canvas', blank)



# paint the canvas w a specific color
blank[:] = 0, 255, 0
cv.imshow('blank_canvas_green', blank)



# paint the canvas w a specific color on specific area
blank[200:300, 300:400] = 0, 0, 255
cv.imshow('blank_canvas_red_square', blank)



# draw a rectangle w a border
cv.rectangle(blank_border_square, (0, 0), (250, 250), (0, 255, 0), thickness=2)
cv.imshow('bordered_rectangle', blank_border_square)



# draw a rectangle w a specific color
cv.rectangle(blank_filled_square, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (0, 255, 0), thickness=cv.FILLED)
cv.imshow('filled__rectangle', blank_filled_square)



# draw a circle 
cv.circle(blank_circle, (250, 250), 40, (0, 0, 255), thickness=-1)
cv.imshow('bordered__circle', blank_circle)



# draw a line 
cv.line(blank_line, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (255, 255, 255), thickness=3)
cv.imshow('line', blank_line)



# write text 
cv.putText(blank_text, 'firedev99', (175, 250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness=2)
cv.imshow('text', blank_text)



cv.waitKey(0)