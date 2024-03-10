import cv2 as cv

# read the image
# img = cv.imread('samples/images/nature_1.jpg')



# rescale image
# works w images, videos, live videos
def rescaleFrame(frame, scale=0.3):
  width = int(frame.shape[1] * scale)
  height = int(frame.shape[0] * scale)
  dimensions = (width, height)

  return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)




# change resoulation of an image
# only works w live video (e.g - webcam)
def changeRes(width, height):
  capture.set(3, width)
  capture.set(4, height)




# how to rescale an image
# # rescales an image
# rescaled_img = rescaleFrame(img)
# cv.imshow('img__resized__2', rescaled_img)
# cv.waitKey(0)
  



# how to rescale a video
# reads the video
capture = cv.VideoCapture('samples/videos/kitten_video_360.mp4')


# show video as fps
while True:
  isTrue, frame = capture.read()
  frame_resized = rescaleFrame(frame)

  # the original frame
  cv.imshow('video__dog', frame)
  # the resized frame
  cv.imshow('video__resized__dog', frame_resized)

  # destroys the window on press key 'd'
  if cv.waitKey(20) & 0xFF==ord('d'):
    break



capture.release()
cv.destroyAllWindows()
