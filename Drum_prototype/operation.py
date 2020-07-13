
import cv2 as cv
import numpy as np

#-----------------------------#
#          blur               #
#-----------------------------#

def blur(kick, snare, hihat):

    reg_kick  = cv.GaussianBlur(kick,  (7, 7), 0)
    reg_snare = cv.GaussianBlur(snare, (7, 7), 0)
    reg_hihat = cv.GaussianBlur(hihat, (7, 7), 0)

    return reg_kick, reg_snare, reg_hihat




#-----------------------------#
#          median             #
#-----------------------------#

def median(kick, snare, hihat):

    median_kick = cv.medianBlur(kick,5)
    median_snare= cv.medianBlur(snare,5)
    median_hihat= cv.medianBlur(hihat,5)

    return median_kick, median_snare, median_hihat

#-----------------------------#
#          bitwise_and        #
#-----------------------------#

def bit_and(kick, snare, hihat, mask_kick, mask_snare, mask_hihat):

    and_kick   = cv.bitwise_and(kick,  kick, mask = mask_kick)
    and_snare  = cv.bitwise_and(snare, snare, mask = mask_snare)
    and_hihat  = cv.bitwise_and(hihat, hihat, mask = mask_hihat)

    return and_kick, and_snare, and_hihat

#-----------------------------#
#       bgr_2_hsv             #
#-----------------------------#

def bgr_2_hsv(kick, snare, hihat):

    hsv_kick  = cv.cvtColor(kick, cv.COLOR_BGR2HSV)
    hsv_snare = cv.cvtColor(snare, cv.COLOR_BGR2HSV)
    hsv_hihat = cv.cvtColor(hihat, cv.COLOR_BGR2HSV)

    return hsv_kick, hsv_snare, hsv_hihat




#-----------------------------#
#          Mask               #
#-----------------------------#

def mask(kick, snare, hihat, lb,ub,lr,ur):

    mask_kick  = cv.inRange(kick,  lb, ub)
    mask_hihat = cv.inRange(hihat, lr, ur)
    mask_snare = cv.inRange(snare, lr, ur)

    return mask_kick, mask_snare, mask_hihat



#-----------------------------#
#     binary_to_gray          #
#-----------------------------#

def binary_2_gray(kick, snare, hihat):

    gray_kick  = cv.cvtColor(kick,  cv.COLOR_BGR2GRAY)
    gray_snare = cv.cvtColor(snare, cv.COLOR_BGR2GRAY)
    gray_hihat = cv.cvtColor(hihat, cv.COLOR_BGR2GRAY)

    return  gray_kick, gray_snare, gray_hihat



#-----------------------------#
#         thesholding         #
#-----------------------------#

def threshold(kick, snare, hihat):

    th_kick = cv.threshold(kick, 15, 255, cv.THRESH_BINARY)[1]
    th_snare = cv.threshold(snare, 15, 255, cv.THRESH_BINARY)[1]
    th_hihat = cv.threshold(hihat, 15, 255, cv.THRESH_BINARY)[1]

    return th_kick, th_snare, th_hihat


#----------------------
# find contours
#----------------------
def findContours(frame):
	cont_frame, hierarchy = cv.findContours(frame, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	return len(cont_frame)
