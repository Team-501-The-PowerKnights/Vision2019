# Only works with mac and Windows 10 currently see comment on line 6 for more instructions
import cv2
import numpy as np
from util.stopwatch import stopwatch as SW

cap = cv2.VideoCapture(0)  # Need to change the 0 to what ever the camera devices name is
timer = SW('timer')
display = "normal"
lastk = 48

while cap.isOpened:
    k = cv2.waitKey(15) & 0xFF
    print(k)
    if k != 255:
        lastk = k
    else:
        k = lastk
    timer.start()
    ret, frame = cap.read()
    new_frame = frame
    if ret:
        print('Got a frame!!')
        frame = cv2.UMat(frame)
        display = "normal_frame"
        cv2.imshow("display", frame)
    if k == 48:
        display = "normal_frame"
        cv2.imshow("display", frame)
        fps = 1.0 / timer.get()
        print('frames per second: %.3f' % fps)
        cv2.putText(frame, str(fps), (20, 20), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0), thickness=1, lineType=2)
    if k == 49:  # Checking if the "1" key is pressed
        hsvup = np.array([186, 209, 142])
        hsvlow = np.array([162, 70, 41])
        mask = cv2.inRange(frame, hsvlow, hsvup)
        cv2.imshow('mask', mask)
        kernel = np.ones((5, 5), np.uint8)
        eroded = cv2.erode(mask, kernel, iterations=4)
        fps = 1.0 / timer.get()
        print('frames per second: %.3f' % fps)
        cv2.putText(eroded, str(fps), (20, 20), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0), thickness=1, lineType=2)
        cv2.imshow('eroded', eroded)
    if k == 50:  # Checking if the "2" key is pressed
        hsvup = np.array([186, 209, 142])
        hsvlow = np.array([162, 70, 41])
        mask = cv2.inRange(frame, hsvlow, hsvup)
        cv2.imshow('mask', mask)
        kernel = np.ones((5, 5), np.uint8)
        dilated = cv2.dilate(frame, kernel, iterations=4)
        cv2.imshow('dilated', dilated)
        fps = 1.0 / timer.get()
        print('frames per second: %.3f' % fps)
        cv2.putText(frame, str(fps), (20, 20), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1, color=(0, 0, 0), thickness=1, lineType=2)
    if k == 27 or k == 113:
        break
