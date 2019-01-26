# Only works with mac currently see comment on line
import cv2
import numpy as np
import sys
from datetime import datetime

cap = cv2.VideoCapture(0)  # Need to change the 0 to what ever the camera devices name is

while cap.isOpened:
    ret, frame = cap.read()
    if ret:
        print('Got a frame!! Yay!')
        frame = cv2.cvtColor(frame,cv2.COLOR_RGB2HSV)
        frame = cv2.UMat(frame)

#    hsvup = np.array([183, 204, 139])
#    hsvlow = np.array([165, 75, 46])

    hsvup = np.array([255, 255, 255])
    hsvlow = np.array([165, 75, 46])

    mask = cv2.inRange(frame, hsvlow, hsvup)

    cv2.imshow('mask', mask)











    cv2.imshow('raw video', frame)
    k = cv2.waitKey(15) & 0xFF
    if k == 27 or k == 113:
        break
