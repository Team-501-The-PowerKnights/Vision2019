# vision2019

FRC Team 501 2019 Python Vision Suite

Pre-requisite Tasks:
- Installing Python3 and openCV on your Pi
https://www.pyimagesearch.com/2018/09/26/install-opencv-4-on-your-raspberry-pi/
- Figure out camera's resolution (Currently is set to 320x240)
- Figure out camera's angle (Currently is set at 60 degrees)


Required software and Libraries:
- mjpg-streamer
https://github.com/jacksonliam/mjpg-streamer
- v4l-utils (from your distro, some do not have it by default)
- PyNetworkTables  `pip install pynetworktables`


A note on usage and philosophy:

Usage of the unix commandline is required for mastery and effective usage of this suite.
We highly suggest holding classes for your students in usage of unix commandline and open source concepts in general.

SSH Security:

The private and public key pair for deployment are included in this repo for our uses.
DO NOT, UNDER ANY CIRCUMSTANCES, USE THIS KEY ON AN INTERNET-CONNECTED SYSTEM.
