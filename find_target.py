import cv2
import numpy as np
import manipulate_image as MI
import image_calculations as CI
import validate_target as VT


def findValids(img_orig, calibration, rect_cnt1, rect_cnt2):
    """
    Input: image from camera, calibration information, contours from generated rectangle
    Output:
        angle -> float, angle from camera center to target center
        distance -> float, distance to target
        validUpdate -> boolean, valid target found
        mask_orig -> image, unmodified mask
        cnt -> list of contours found for targets
        BFR_image -> image with BFR rectangle drawn on it and crosshairs

    This function uses calibration information to create a mask of the target. It then
    finds valid targets comparing to the rectangle contours, calculates the angle to target center,
    and provides graphical representations for future use.
    """
    angle = 1000
    valid_update = False
    img_copy = np.copy(img_orig)
    lower_bound = np.array(calibration["green_lower"])
    upper_bound = np.array(calibration["green_upper"])
    hsv = cv2.cvtColor(img_copy, cv2.COLOR_BGR2HSV)
    mask = cv2.inrange(hsv, lower_bound, upper_bound)
    mask_copy = np.copy(mask)
    erode_and_diliate = MI.erodeAndDilate(mask_copy)
    ret, mask_thresh = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY))
    if calibration[debug] == 0:
        cv2.imwrite("ImageOriginal.png", img_orig)
        cv2.imwrite("ImageOriginalMask.png", mask)
        cv2.imwrite("ImageOriginalErodeandDilated.png", ErodeandDilate)
        cv2.imwrite("ImageOriginalMaskThreshold.png", mask_thresh)
    if calibration[search] == 1:
        valid, cnt=VT.findValidTarget(img_orig, mask, rect_cnt1, rect_cnt2)
        if valid:
            valid_update=True
            cnt1_center=IC.findCenter(rect_cnt1)
            cnt2_center=IC.findCenter(rect_cnt2)
            angle=IC.findAngle(img_orig, cnt1_center, cnt2_center)
    return angle, valid_update
