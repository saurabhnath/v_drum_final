#import all files
import cv2 as cv
import numpy as np
from frame import capture, play_video, save_img
from roi import draw_drum, roi, stick_color
from operation import blur, binary_2_gray, threshold, mask,bgr_2_hsv, median, bit_and, findContours
from execution import execute
from music import play_sound

#capture frame from the web camera:
web_cam = cv.VideoCapture(0)

k = 0
s = 0
h = 0


#main function:
while True:
    #read frame:
    frame = capture(web_cam)

    #region of interest:
    kick, snare, hihat = roi(frame)

    #blur the region:
    blur_kick, blur_snare, blur_hihat = blur(kick, snare, hihat)

    #stick colors:
    lb, ub, lr, ur = stick_color()

    # bgr to hsv:
    hsv_kick, hsv_snare, hsv_hihat = bgr_2_hsv(blur_kick, blur_snare, blur_hihat)

    # mask regions for traking stick color:
    mask_kick,  mask_snare, mask_hihat = mask(hsv_kick, hsv_snare, hsv_hihat, lb, ub, lr, ur )

    #tracking the stick color:
    and_kick, and_snare, and_hihat = bit_and( kick, snare, hihat, mask_kick,  mask_snare, mask_hihat)

    #convert regions to gray:
    gray_kick, gray_snare, gray_hihat = binary_2_gray( and_kick, and_snare, and_hihat)

    #thesholding the regions:
    th_kick, th_snare, th_hihat = threshold(gray_kick, gray_snare, gray_hihat)

    # median filter to remove salt-papper noise:
    median_kick, median_snare, median_hihat = median(th_kick, th_snare, th_hihat)
    #execute to get input:

    w_kick, w_snare, w_hihat, k, s, h = execute(median_kick, median_snare, median_hihat, k, s, h)

    #play music
    play_sound(w_kick, w_snare, w_hihat)

    #draw the drum regions:
    draw_drum(frame)

    #show video frame:
    play_video('web_cam_video', frame)
    #play_video('reg_kick', th_kick)
    #play_video('reg_snare', th_snare)
    #play_video('reg_hihat', th_hihat)

    #quit from the video
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    #save image:
    elif cv.waitKey(1) & 0xFF == ord('s'):
        save_img(frame)


#release webcam:
web_cam.release()
#destroy all windows:
cv.destroyAllWindows()
