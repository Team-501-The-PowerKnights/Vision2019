#!/usr/bin/env bash

# init video stream at 60fps at 320x240
mjpg_streamer -o "output_http.so -w ./www -p 1180" -i "input_uvc.so -d /dev/video0 -f 30 -r 640x480 -n" &

# turns off auto-exposure
v4l2-ctl --set-ctrl exposure_auto=1
# sets exposure value to 20
v4l2-ctl --set-ctrl exposure_absolute=15

# disable auto white-balance, set to 5000K
v4l2-ctl --set-ctrl white_balance_temperature_auto=0
v4l2-ctl --set-ctrl white_balance_temperature=5000
echo "done"