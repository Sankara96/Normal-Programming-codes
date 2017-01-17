import numpy as np
import cv2
import time

face_cascade = cv2.CascadeClassifier(r'D:\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(r'D:\opencv\sources\data\haarcascades\haarcascade_eye_tree_eyeglasses.xml')
#time.sleep(10)
# img = cv2.imread(r'E:\Mini_project\opencv_haar\positive_images\image_1.jpg')
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    if ret == 0:
        continue
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face = face_cascade.detectMultiScale(img_gray, 1.3, 5)
    print face
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow('img', img)
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        break

