import cv2 as cv
import numpy as np


#**************************
#Drum regions of interest:
#**************************
def roi(frame):
    x = 370
    #kick region of interest: using the key word k:
    k_top, k_buttom, k_right, k_left = 550, 710, 380, 150
    #snare region of interest: Key-word: s
    s_top, s_buttom, s_right, s_left = k_top  , k_buttom , k_right + x, k_left + x
    #Hithat region of interest: key-word is h:
    h_top, h_buttom, h_right, h_left = k_top , k_buttom , k_right + 2*x, k_left + 2*x

    r_kick = frame[k_top:k_buttom, k_left:k_right]
    r_snare = frame[s_top:s_buttom, s_left: s_right]
    r_hithat = frame[h_top:h_buttom, h_left:h_right]


    return r_kick, r_snare, r_hithat


#*****************************

#img = cv.imread('new.jpeg')
#kick,hithat, snare = roi(img)
#cv.imshow('new', kick)
#cv.imshow('new1', hithat)
#cv.imshow('new2', snare)
#cv.waitKey(0)
#cv.destroyAllWindows()

#---------------------------------------------------------
#stick color:
#---------------------------------------------------------
# we have choosen two color sticks: all are in HSV format
# blue: -----> for kick only
# red: -----> for both hithat and r_snare

def stick_color():

    lower_blue =  np.array([108,154,90])
    upper_blue =  np.array([133,255,255])

    lower_red =  np.array([00,162,162])
    upper_red =  np.array([54,255,255])

    return lower_blue,upper_blue,lower_red,upper_red
#--------------------------------------------------------



#*****************
#drum graphics:
#*****************
def draw_drum(frame):
    x = 370

    # kick region:
    k1 = (150, 550)
    k2 = (380, 710)
    k3 = (230, 645)

    #snare
    s1 = (150+x, 550)
    s2 = (380+x, 710)
    s3 = (230+x, 645)

    #hihat
    h1 = (150+2*x, 550)
    h2 = (380+2*x, 710)
    h3 = (230+2*x, 645)

    #draw kick:
    cv.rectangle(frame,k1,k2,(255,200,73),3)
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(frame,'kick', k3,font, 1,(0,255,0),2,cv.LINE_AA)
    #draw snare
    cv.rectangle(frame,s1,s2,(45,100,250),3)
    cv.putText(frame,'snare', s3, font, 1,(0,255,0),2,cv.LINE_AA)
    #draw hihat:
    cv.rectangle(frame,h1,h2,(45,100,250),3)
    cv.putText(frame,'hihat', h3, font, 1,(0,255,0),2,cv.LINE_AA)


    cv.putText(frame,'Virtual Drum,    final project-2020, ECE', (150,50), font, 1,(0,157,255),2,cv.LINE_AA)
