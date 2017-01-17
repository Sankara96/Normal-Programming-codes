import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)  # 640,480
w = 640
h = 480


while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        # downsample
        # frameD = cv2.pyrDown(cv2.pyrDown(frame))
        # frameDBW = cv2.cvtColor(frameD,cv2.COLOR_RGB2GRAY)

        # detect face
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        faces = cv2.CascadeClassifier(r'D:\opencv\sources\data\haarcascades\haarcascade_lefteye_2splits.xml')
        detected = faces.detectMultiScale(frame, 1.3, 5)

        pupilFrame = frame

        pupilO = frame
        windowClose = np.ones((5, 5), np.uint8)
        windowOpen = np.ones((2, 2), np.uint8)
        windowErode = np.ones((2, 2), np.uint8)

        # draw square
        for (x, y, w, h) in detected:
            cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (0, 0, 255), 1)
            cv2.line(frame, (x, y), ((x + w, y + h)), (0, 0, 255), 1)
            cv2.line(frame, (x + w, y), ((x, y + h)), (0, 0, 255), 1)
            pupilFrame = cv2.equalizeHist(frame[y + (h * .25):(y + h), x:(x + w)])
            pupilO = pupilFrame
            ret, pupilFrame = cv2.threshold(pupilFrame, 70, 255, cv2.THRESH_BINARY)  # 50 ..nothin 70 is better
            pupilFrame = cv2.morphologyEx(pupilFrame, cv2.MORPH_CLOSE, windowClose)
            pupilFrame = cv2.morphologyEx(pupilFrame, cv2.MORPH_ERODE, windowErode)
            pupilFrame = cv2.morphologyEx(pupilFrame, cv2.MORPH_OPEN, windowOpen)
        time.sleep(3)
        canny_frame = cv2.Canny(frame, 100, 200)
        circles = cv2.HoughCircles(frame,cv2.cv.CV_HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            cv2.circle(Frame,(i[0],i[1]),i[2],(0,255,0),2)

            cv2.circle(Frame,(i[0],i[1]),2,(255,0,0),3)
        cv2.imshow("image_frame",frame)
        cv2.imshow("image_pupilframe", pupilFrame)
        cv2.imshow("Canny-edge",canny_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

            # else:
            # break

    # Release everything if job is finished
cap.release()
cv2.destroyAllWindows()