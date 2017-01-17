import numpy as np
import cv2
import serial

arduino = serial.Serial('COM4',9600,timeout=.1)
arduino.
arduino.close()

def nothing(x):
    pass


cap = cv2.imread(r'C:\Users\ADMIN\Desktop\tennis-ball.jpg')

cv2.namedWindow('Image', cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('H', 'Image', 0, 179, nothing)
cv2.createTrackbar('S', 'Image', 0, 255, nothing)
cv2.createTrackbar('I', 'Image', 0, 255, nothing)
# LOW values of HSV values
cv2.createTrackbar('Hl', 'Image', 0, 179, nothing)
cv2.createTrackbar('Sl', 'Image', 0, 255, nothing)
cv2.createTrackbar('Il', 'Image', 0, 255, nothing)
while (True):
    hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)
    H = cv2.getTrackbarPos('H', 'Image')
    S = cv2.getTrackbarPos('S', 'Image')
    I = cv2.getTrackbarPos('I', 'Image')
    Hl = cv2.getTrackbarPos('Hl', 'Image')
    Sl = cv2.getTrackbarPos('Sl', 'Image')
    Il = cv2.getTrackbarPos('Il', 'Image')
    front = cv2.inRange(hsv, (Hl, Sl, Il), (H, S, I))
    cv2.namedWindow('front', cv2.WINDOW_AUTOSIZE)
    # cv2.namedWindow('back',cv2.WINDOW_NORMAL)
    # cv2.namedWindow('dest',cv2.WINDOW_NORMAL)
    cv2.imshow('front', hsv)
    # cv2.imshow('back',back)
    # cv2.imshow('dest',dest)
    cv2.namedWindow('frame', cv2.WINDOW_AUTOSIZE)

    cv2.imshow('frame', cap)
    if cv2.waitKey(1)==27:
       break

cap.release()
cv2.destroyAllWindows()