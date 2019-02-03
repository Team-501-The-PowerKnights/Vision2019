import cv2
import numpy as np
import manipulate_image as MI
import image_calculations as CI
import validate_target as VT


def findValids(img_orig, calibration, rect_cnt):
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
    # initialize variables
    # convert image into HSV
    # create mask with lower and upper hsv bounds
    # Clean up mask with dilate and erode and threshold
    # if debug: write original frame, original mask, eroded and dilated mask, and mask threshold
    # if search: call findValidTarget
    # if valid: update validUpdate, find center of each target, find angle to target, find distance to target
    pass