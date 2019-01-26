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
        frame = cv2.UMat(frame)

    cv2.imshow('raw video', frame)
    k = cv2.waitKey(15) & 0xFF
    if k == 27 or k == 113:
        break
