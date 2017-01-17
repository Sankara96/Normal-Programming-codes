# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import cv2

o = 0
# pink
hp = 179
sp = 93
ip = 217
hpl = 144
spl = 51
ipl = 134
# yellow
hyl = 7
Syl = 52
iyl = 152

hy = 147
sy = 255
iy = 255
# blue
hl = 94
sl = 103
il = 43
h = 133
s = 206
i = 203


def nothing(x):
    pass


cap = cv2.VideoCapture(1)
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.createTrackbar('H', 'Image', 0, 179, nothing)
cv2.createTrackbar('S', 'Image', 0, 255, nothing)
cv2.createTrackbar('I', 'Image', 0, 255, nothing)
# LOW values of HSV values
cv2.createTrackbar('Hl', 'Image', 0, 179, nothing)
cv2.createTrackbar('Sl', 'Image', 0, 255, nothing)
cv2.createTrackbar('Il', 'Image', 0, 255, nothing)
while (1):
    ret, frame = cap.read()
    if ret == 0:
        continue

    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # HIGH vaLues of HSV values


    H = cv2.getTrackbarPos('H', 'Image')
    S = cv2.getTrackbarPos('S', 'Image')
    I = cv2.getTrackbarPos('I', 'Image')
    Hl = cv2.getTrackbarPos('Hl', 'Image')
    Sl = cv2.getTrackbarPos('Sl', 'Image')
    Il = cv2.getTrackbarPos('Il', 'Image')
    front = cv2.inRange(img_hsv, (Hl, Sl, Il), (H, S, I))
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    front = cv2.erode(front, kernel)
    front = cv2.dilate(front, kernel)
    # contoursf,hierarchyf=cv2.findContours(front,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    # for i in range(0,len(contoursf)-1):
    # area=cv2.contourArea(contoursf[i])
    # if(area>100):
    #  o=o+1;
    # M1=cv2.moments(contoursf[0])
    # xf=int(M1['m10']/M1['m00'])
    # yf=int(M1['m01']/M1['m00'])
    # cv2.circle(frame,(xf,yf),1,(0,0,0),2)
    # print o
    #  print xf,yf

    # blur = cv2.GaussianBlur(img_bin,(5,5),1)
    # th3 = cv2.adaptiveThreshold(img_bin,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
    # cv2.THRESH_BINARY,11,2)
    #   th4 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
    # cv2.THRESH_BINARY,11,2)
    #   edges = cv2.Canny(frame,100,200)
    # ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    # image, contours = cv2.findContours(img_bin,1,2)
    # img = cv2.drawContours(img_bin, contours, -1, (0,255,0), 3)
    # cnt = contours[0]
    # M = cv2.moments(cnt)
    # print M
    # hull = cv2.convexHull(edges)
    cv2.imshow('Binary image', front)
    #  cv2.imshow('Canny edge detection',edges)
    # cv2.imshow('Contours',hull)
    # cv2.imshow('Adaptive thresholding Binary image without filter',th3)
    # cv2.imshow('Adaptive thresholding Binary image with filter',th4)
    cv2.imshow('Original image', frame)
    cv2.imshow('HSV image', img_hsv)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()