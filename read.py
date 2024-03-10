import cv2 as cv

# # reads the image
# img = cv.imread('images/pexels_1.jpg')
# # shows the image itself
# cv.imshow('img__1', img)


# # waits until it's destroyed
# cv.waitKey(0)



# read the video
capture = cv.VideoCapture('samples/videos/dog_video_360.mp4')


while True:
  # read the status and fps
  isTrue, frame = capture.read() 
  # shows the frame per second
  cv.imshow('video__dog', frame)

  # if the letter D was pressed destroy the window
  if cv.waitKey(20) & 0xFF==ord('d'):
    break




# destroys the window on video end
capture.release()
cv.destroyAllWindows()

