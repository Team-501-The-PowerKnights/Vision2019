import cv2
import numpy as np
import time
import sys
sys.path.append('/usr/local/lib')
import logging
from datetime import datetime

from util.config import runConfig
from networktables import NetworkTables
import find_target as FT

logging.basicConfig(level=logging.DEBUG)

os, camera_location, calibration, freqFramesNT, vertx, verty = runConfig(None)

# Vision.angle (double)
# Vision.locked (boolean)
# Vision.count (integer)



def main():
    # initialize network tables
    # initialize camera
    # create rectangle shape representing target
    # run main loop of vision program
    pass


def nt_init():
    """
    Initialize network tables
    :parameter None
    :return camera network table
    """
    #NetworkTables.setIPAddress('10.5.1.141')
    #NetworkTables.setClientMode()
    #NetworkTables.initialize(server='10.5.1.141')
    # port 1735
    pass


def create_rect():
    """
        Creates a rectangle and performs appropriate processing to provide a target
        returns the contour object of the rectangle
        :return the two contours of the rectangle we want to validate targets
        against (returned as a tuple)
        """
    # Draw rectangles of the retro reflective tape (Find dimensions in the game manual)
    # Camera dimensions: 320 x 240
    # Rectangle dimensions: 40 x 110
    width = 40
    length = 110
    img_width = 175
    img_length = 175

    top_left_x = int(img_width - width / 2)
    top_left_y = int(img_length - length / 2)
    bottom_right_x = int(img_width + width / 2)
    bottom_right_y = int(img_length + length / 2)

    background = np.zeros((350, 350, 3), np.uint8)
    rect1 = cv2.rectangle(background, (top_left_x, top_left_y), (bottom_right_x, bottom_right_y), (255, 255, 255), -1)
    m = cv2.getRotationMatrix2D((350 / 2, 350 / 2), -14.5, 1)
    rect1_rotated = cv2.warpAffine(rect1, m, (350, 350))
    ret, thresh = cv2.threshold(rect1_rotated, 127, 255, cv2.THRESH_BINARY)
    image, contours, hierrchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt1 = contours[0]

    rect2 = rect1
    m = cv2.getRotationMatrix2D((350 / 2, 350 / 2), 14.5, 1)
    rect2_rotated = cv2.warpAffine(rect2, m, (350, 350))
    ret, thresh = cv2.threshold(rect2_rotated, 127, 255, cv2.THRESH_BINARY)
    image, contours, hierrchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt2 = contours[0]
    return cnt1, cnt2


def nt_send(camera_table, Angle, validCount, validUpdate):
    """
    Send relevant data to the network table
    :param camera_table: camera network table
    :param Angle: angle to target
    :param validCount: number of valid updates we have found
    :param validUpdate: boolean True if valid target found, false otherwise
    :return: None
    """
    pass


def cap_init(camera_location):
    """
    Initialize camera
    :param camera_location: what the camera url is
    :return: cap returned from cv2.VideoCapture
    """
    pass


def run(cap, camera_table, calibration, freqFramesNT, rect_cnt):
    """
    Run the main vision algorithm on each camera frame and update network table appropriately
    :param cap: cap returned from cv2.VideoCapture
    :param camera_table: the network table we are writing to
    :param calibration: dictionary containing hsv thresholds and whether we are in debug mode or not
    :param freqFramesNT: frequency of frames for data to be sent to network tables
    :param rect_cnt: contour of the rectangle we want to validate targets against
    :return: None
    """
    pass
    # initialize validCount and frame number
    validCount = 0
    n = 0
    # while cap is open
        # read frame
        # call findValids on frame
        # update validCount
        # if frame number greater than freqFramesNT send data to network table


if __name__ == "__main__":
    # execute only if run as a script
    main()
