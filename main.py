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
    camera_table = nt_init()
    cap = cap_init(camera_location)
    rect_cnt1, rect_cnt2 = create_rect()
    run(cap, camera_table, calibration, freqFramesNT, rect_cnt1, rect_cnt2)


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
    pass


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
    try:
        cap = cv2.VideoCapture(eval(camera_location))
        time.sleep(1)
    except:
        print("Exception on VideoCapture init. Dying")
        sys.exit()
    return cap



def run(cap, camera_table, calibration, freqFramesNT, rect_cnt1, rect_cnt2):
    """
    Run the main vision algorithm on each camera frame and update network table appropriately
    :param cap: cap returned from cv2.VideoCapture
    :param camera_table: the network table we are writing to
    :param calibration: dictionary containing hsv thresholds and whether we are in debug mode or not
    :param freqFramesNT: frequency of frames for data to be sent to network tables
    :param rect_cnt: contour of the rectangle we want to validate targets against
    :return: None
    """
    valid_count = 0
    n = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            try:
                angle, valid_update = FT.find_valids(frame, calibration, rect_cnt1, rect_cnt2)
                if valid_update:
                    valid_count += 1
                if n > freqFramesNT:
                    nt_send(camera_table, angle, valid_count, valid_update)
                    n = 0
                else:
                    n += 1
            except:
                print("There was an error with find_valids. Continuing.")
        else:
            print("Unable to read frame. Continuing.")
    else:
        print("Capture is not opened. Ending program.")


if __name__ == "__main__":
    # execute only if run as a script
    main()