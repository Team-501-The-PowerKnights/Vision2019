"""
Created on Tues Feb 19 08:40:34 2019

@author: Matt-Gleich & dithier

Other important info:
You need to change the camera resolution from 320x240 to you camera's res
"""
import cv2
import numpy as np


def erodeAndDilate(img):
    """
    Erodes and then dilates the mask of the image
    :param img: the image frame mask being analyzed
    :return: and eroded and dilated image
    """
    kernel = np.ones((5, 5), np.unit8)
    erosion = cv2.erode(img, kernel, iterations=1)
    erosion_and_dilation = cv2.dilate(erosion, kernel, iterations=1)
    return erosion_and_dilation


def drawLine2Target(img, cx, cy):
    """
    Draws a line from the center of the camera point of view to the center of the target
    :param image: the original frame
    :param cx: x coordinate of target center
    :param cy: y coordinate of target center
    :return: image with a line drawn to target
    """
    img_line = cv2.line(img, (160, 120), (cx, cy), (255, 0, 0), 2)
    return img_line


def drawCrossHairs(img):
    """
    Draws crosshairs in image donating the center of the camera view
    :param image: the image being analyzed
    :return: an image with crosshairs drawn
    """
    top_hair = cv2.line(img, (160, 130), (160, 150), (0, 0, 255), 3)
    bottom_hair = cv2.line(top_hair, (160, 110), (160, 90), (0, 0, 255), 3)
    left_hair = cv2.line(bottom_hair, (150, 120), (120, 120), (0, 0, 255), 3)
    crosshairs = cv2.line(left_hair, (170, 130), (190, 120), (0, 0, 255), 3)
    return crosshairs
