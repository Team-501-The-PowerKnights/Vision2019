# Only works with mac currently see comment on line
import cv2
import numpy as np
import sys
from datetime import datetime
import time
from util.stopwatch import stopwatch

cap = cv2.VideoCapture(0)  # Need to change the 0 to what ever the camera devices name is

timer = stopwatch("FPS")


while cap.isOpened:
    ret, frame = cap.read()
    timer.start()
    if ret:
        frame = cv2.UMat(frame)
    cv2.imshow('raw video', frame)
    k = cv2.waitKey(15) & 0xFF
    fps = 1 / timer.get()
    print(fps)
    if k == 27 or k == 113:
        break
