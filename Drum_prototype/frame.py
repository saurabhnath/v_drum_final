# to read frames
#flip the frames
#display the frames
import cv2 as cv

#read frames:
def capture(web_cam):
    ret, frame = web_cam.read()
    frame = cv.flip(frame, 1)
    return frame

#display
def play_video(name,frame):
    cv.imshow(name, frame)

#save frame:
def save_img(frame):
    cv.imwrite('new.jpeg',frame)
