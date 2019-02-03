import cv2
import numpy as np

def bestFitRect(img_orig, cnt):
    """

    :param img_orig: the image frame being analyzed
    :param cnt: the contour of the potential target
    :return: corners of the rectangle
            original image with BFR and corners drawn on it
    """
    # Find convex hull
    # Create black image, draw rectangle hull on it, corner detection
    # Find coordinates for the four corners
    # Load original image and draw BFR and corners
    pass

def erodeAndDilate(img):
    """
    Erodes and then dilates the mask of the image
    :param img: the image frame mask being analyzed
    :return: and eroded and dilated image
    """
    pass


def drawLine2Target(image, cx, cy):
    """
    Draws a line from the center of the camera point of view to the center of the target
    :param image: the original frame
    :param cx: x coordinate of target center
    :param cy: y coordinate of target center
    :return: image with a line drawn to target
    """
    pass


def drawCrossHairs(image):
    """
    Draws crosshairs in image donating the center of the camera view
    :param image: the image being analyzed
    :return: an image with crosshairs drawn
    """
    pass