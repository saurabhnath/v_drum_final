import cv2 as cv
import numpy as np

def nothing(x):
    pass

cv.namedWindow("color_Tracking")
cv.createTrackbar("LH", "color_Tracking", 0, 255, nothing)
cv.createTrackbar("LS", "color_Tracking", 0, 255, nothing)
cv.createTrackbar("LV", "color_Tracking", 0, 255, nothing)
cv.createTrackbar("UH", "color_Tracking", 0, 255, nothing)
cv.createTrackbar("US", "color_Tracking", 0, 255, nothing)
cv.createTrackbar("UV", "color_Tracking", 0, 255, nothing)
cap = cv.VideoCapture(0)
while True:
    _,frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    l_h = cv.getTrackbarPos("LH", "color_Tracking")
    l_s = cv.getTrackbarPos("LS", "color_Tracking")
    l_v = cv.getTrackbarPos("LV", "color_Tracking")

    u_h = cv.getTrackbarPos("UH", "color_Tracking")
    u_s = cv.getTrackbarPos("US", "color_Tracking")
    u_v = cv.getTrackbarPos("UV", "color_Tracking")

    l = np.array([l_h, l_s, l_v])
    u = np.array([u_h, u_s, u_v])

    mask = cv.inRange(hsv, l, u)
    #blur = cv.GaussianBlur(mask,(5,5),0)
    median = cv.medianBlur(mask,9)
    res = cv.bitwise_and(frame, frame, mask = mask)
    cv.imshow('mask',median)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
