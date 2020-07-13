import cv2 as cv2
import numpy as np
from operation import findContours


def execute(kick, snare, hihat, b_kick, b_snare, b_hihat):

    play_kick, play_snare, play_hihat = False, False, False

    count_kick = findContours(kick)
    count_snare = findContours(snare)
    count_hihat = findContours(hihat)

    if (count_kick > 0) and (b_kick == 0):
        play_kick = True
        b_kick = 1
    elif (count_kick == 0):
        b_kick = 0


    if (count_snare > 0) and (b_snare == 0):
        play_snare = True
        b_snare = 1
    elif (count_snare == 0):
        b_snare = 0

    if (count_hihat > 0) and (b_hihat == 0):
        play_hihat = True
        b_hihat = 1
    elif (count_hihat == 0):
        b_hihat = 0

    return play_kick, play_snare, play_hihat, b_kick, b_snare, b_hihat
