import cv2
import numpy as np
import imageCalculationsS as IC
from heapq import nlargest
import manipulateImageS as MI

def isValidShape(contour, rect_cnt):
    """
    Use cv2.matchShapes to see if the contour is close enough to the shape we are looking for
    :param contour: contour of potential target being analyzed
    :param rect_cnt: contour of what the perfect target should be
    :return: boolean, True if the shape match is within the allowable threshold, False otherwise
    """
    pass


def findValidTarget(image, mask, rect_cnt):
    """

    :param image: frame to be analyzed
    :param mask: mask of thresholded hsv image
    :param rect_cnt: contour of perfect target rectangle
    :return: valid: boolean, True if valid target, False otherwise
            cnt: list where first entry is the contour of target 1 and second entry is contour of target 2
            Rect_coor: nested list of each corner coordinate for the targets
            BFR_img: a copy of the image being analyzed (if in debug mode has BFR drawn on it and corners and lines
            to center"
    """
    # initialize variables
    # find contours
    # take 6 longest contours
    # Determine area of each contour and sort by largest to smallest
    # Check for validity of contours in order of largest area to smallest
    # do shape match
    # if shape match is valid do best fit rectangle, and if 4 corners update cnt, Rect_coor, and goodTarget
    # otherwise analyze next contour
    # after loop is done update valid and return other outputs
    pass