# Only works with mac currently see comment on line
import cv2
import numpy as np
from util.stopwatch import stopwatch as SW

cap = cv2.VideoCapture(0)  # Need to change the 0 to what ever the camera devices name is
timer = SW('timer')


while cap.isOpened:
    timer.start()
    ret, frame = cap.read()
    if ret:
        print('Got a frame!! Yay!')
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        frame = cv2.UMat(frame)


    hsvup = np.array([186, 209, 142])
    hsvlow = np.array([162, 70, 41])
    mask = cv2.inRange(frame, hsvlow, hsvup)
    cv2.imshow('mask', mask)

    kernel = np.ones((5, 5), np.uint8)
    eroded = cv2.erode(mask,kernel,iterations=4)
    cv2.imshow('eroded', eroded)
    dilated = cv2.dilate(eroded,kernel,iterations=4)
    cv2.imshow('dilated', dilated)
    fps = 1.0 / timer.get()
    print('frames per second: %.3f' % fps)
    cv2.putText(frame, str(fps), (20,20), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(255,255,255), thickness=1, lineType=2)
    cv2.imshow('raw video', frame)









    k = cv2.waitKey(15) & 0xFF
    if k == 27 or k == 113:
        break
