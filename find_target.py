import cv2
import numpy as np
import manipulate_image as MI
import validate_target as VT
from util.stopwatch import stopwatch as SW

def find_valids(img_orig, calibration, rect_cnt1, rect_cnt2):
    """
    Input: image from camera, calibration information, contours from generated rectangle
    Output:
        angle -> float, angle from camera center to target center
        validUpdate -> boolean, valid target found

    This function uses calibration information to create a mask of the target. It then
    finds valid targets comparing to the rectangle contours, calculates the angle to target center,
    and provides graphical representations for future use.
    """
    debug = calibration['debug']
    search = calibration['search']
    angle = 1000
    valid_update = False
    img_copy = np.copy(img_orig)
    lower_bound = np.array(calibration["green"]["green_lower"])
    upper_bound = np.array(calibration["green"]["green_upper"])
    if debug:
        timer_ft = SW('ft')
        timer_ft.start()
    hsv = cv2.cvtColor(img_copy, cv2.COLOR_BGR2HSV)
    if debug:
        elapsed=timer_ft.get()
        print("DEBUG: cvt took " + str(elapsed))
    if debug:
        timer_ft.start()
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    if debug:
        elapsed = timer_ft.get()
        print("DEBUG: inrange took "+ str(elapsed))
    if debug:
        timer_ft.start()
    erode_and_diliate = MI.erodeAndDilate(mask)
    if debug:
        elapsed = timer_ft.get()
        print("DEBUG: erode_and_dilate took "+ str(elapsed))
    if debug:
        timer_ft.start()
    ret, mask_thresh = cv2.threshold(erode_and_diliate, 127, 255, cv2.THRESH_BINARY)
    if debug:
        elapsed = timer_ft.get()
        print("DEBUG: threshold took "+ str(elapsed))
    if search:
        valid, cnt, cx, cy = VT.find_valid_target(mask_thresh, rect_cnt1, rect_cnt2)
        if valid:
            valid_update = True
            # angle = IC.findAngle(cx[0], cx[1])
    return angle, valid_update
