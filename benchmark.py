import cv2
from util.stopwatch import stopwatch as SW
import numpy as np

cap = cv2.VideoCapture(0)

timer0 = SW('0')
timer1 = SW('1')

kernel = np.ones((5, 5), np.uint8)
hsvup = np.array([186, 209, 142])
hsvlow = np.array([162, 70, 41])

while cap.isOpened():
    ret, frame = cap.read()
    normal = frame
    if ret:
        umat_mat = cv2.UMat(frame)
    else:
        break

    timer0.start()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv = cv2.inRange(hsv, hsvlow, hsvup)
    hsv = cv2.erode(hsv, kernel, iterations=4)
    hsv = cv2.dilate(hsv, kernel, iterations=4)
    normal_time = timer0.get()

    timer1.start()
    umat_hsv = cv2.cvtColor(umat_mat, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(umat_hsv, hsvlow, hsvup)
    eroded = cv2.erode(mask, kernel, iterations=4)
    dilated = cv2.dilate(eroded, kernel, iterations=4)
    normal_time = timer0.get()









    umat_time = timer1.get()

    print('normal: %.5f' % (normal_time))
    print('n.umat: %.5f' % (umat_time))










