# Identify pupils. Based on beta 1

import numpy as np
import cv2
import time

time.sleep(10)

cap = cv2.VideoCapture(1)  # 640,480
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
        faces = cv2.CascadeClassifier(r'D:\opencv\sources\data\haarcascades\haarcascade_eye.xml')
        detected = faces.detectMultiScale(frame, 1.3, 5)
        #print detected
        #if len(detected) > 0:
        #   detected = [detected[0]]
        # faces = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        # detected2 = faces.detectMultiScale(frameDBW, 1.5, 8)

        pupilFrame = frame
        pupilO = frame
        windowClose = np.ones((5, 5), np.uint8)
        windowOpen = np.ones((2, 2), np.uint8)
        windowErode = np.ones((2, 2), np.uint8)

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

            # so above we do image processing to get the pupil..
            # now we find the biggest blob and get the centriod

            threshold = cv2.inRange(pupilFrame, 250, 255)  # get the blobs
            contours, hierarchy = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

            # if there are 3 or mo)re blobs, delete the biggest and delete the left most for the right eye
            # if there are 2 blob, take the second largest
            # if there are 1 or less blobs, do nothing

            if len(contours) >= 2:
                # find biggest blob
                maxArea = 0
                MAindex = 0  # to get the unwanted frame
                distanceX = []  # delete the left most (for right eye)
                currentIndex = 0
                for cnt in contours:
                    area = cv2.contourArea(cnt)
                    center = cv2.moments(cnt)
                    center2 = center['m00']
                    if center2 == 0:
                        center2 = 1
                    cx, cy = int(center['m10'] / center2), int(center['m01'] / center2)
                    distanceX.append(cx)
                    if area > maxArea:
                        maxArea = area
                        MAindex = currentIndex
                    currentIndex = currentIndex + 1

                del contours[MAindex]  # remove the picture frame contour
                del distanceX[MAindex]

            eye = 'right'

            if len(contours) >= 2:  # delete the left most blob for right eye
                if eye == 'right':
                    edgeOfEye = distanceX.index(min(distanceX))
                else:
                    edgeOfEye = distanceX.index(max(distanceX))
                del contours[edgeOfEye]
                del distanceX[edgeOfEye]

            if len(contours) >= 1:  # get largest blob
                maxArea = 0
                for cnt in contours:
                    area = cv2.contourArea(cnt)
                    if area > maxArea:
                        maxArea = area
                        largeBlob = cnt

            if len(largeBlob) > 0:
                center = cv2.moments(largeBlob)
                center1 = center['m00']
                if center1 == 0:
                    center1 = 1
                cx, cy = int(center['m10'] / center1), int(center['m01'] / center1)
                cv2.circle(pupilO, (cx, cy), 10, 255, -1)
                print "x:{0} y:{1}".format(cx,cy)

        # show picture
        cv2.imshow("Original_image",frame)
        cv2.imshow('frame', pupilO)
        cv2.imshow('frame2', pupilFrame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

            # else:
            # break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()