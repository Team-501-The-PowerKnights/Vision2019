from stopwatch import stopwatch as SW
import os
import sys
from networktables import NetworkTables as NT
import socket
from collections import namedtuple
import time

"""
telemetry push system 

****
ONLY WORKS ON LINUX, DO NOT EVEN BOTHER TRYING ON MAC OR WINDOWS.
****





"""

def main():
    table = telemetry_init()
    telemetry_run(table)


def telemetry_init():
    ROBOT = 'roborio-501-frc.local'  # set robot name
    ROBOT_IP = socket.gethostbyname(ROBOT)  # determine robot IP
    print('connecting to roborio at %s' % ROBOT_IP)

    try:
        NT.initialize(server=ROBOT_IP)
        init = True
    except:
        print("Unable to initialize network tables.")
        init = False
    try:
        vision_table = NT.getTable('SmartDashboard')
    except:
        print("unable to get vision table")
        NT.stop()
        NT.destroy()
        init = False
    if not init:
        time.sleep(1)
        print("retrying networktables initialization.")
    else:
        print("vision table acquired")
        vision_table.putBoolean('connected', True)
        pullback = vision_table.getBoolean('connected', None)
        print('pullback: %r' % pullback)
        return vision_table

def telemetry_run(vision_table):
    while(True):
        with open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq') as f:  # read CPU frequency
            cpu_freq = int(f.read())
        f.closed
        MHz = int(cpu_freq / 1000.0)
        clock_speed = str(MHz) + ' MHz'
        print(clock_speed)
        vision_table.putString('RPI/Clock Speed', clock_speed)

        with open('/sys/class/thermal/thermal_zone0/temp') as f:  # read SOC temperature
            soc_temp = int(f.read())
        f.closed
        soc_temp = str(int(soc_temp / 1000)) + ' C'
        print(soc_temp)
        vision_table.putString('RPI/SOC Temp', soc_temp)

        MemInfoEntry = namedtuple('MemInfoEntry', ['value', 'unit'])  # gets memory information
        mem_info = {}
        with open('/proc/meminfo') as file:
            for line in file:
                key, value, *unit = line.strip().split()
                mem_info[key.rstrip(':')] = MemInfoEntry(value, unit)
        free_memory = str(int(int(mem_info['MemFree'][0]) / 1000 )) + ' MB'
        print(free_memory)
        vision_table.putString('RPI/Free Memory', free_memory)


        # print(mem_info['SwapFree'][0])
        # print(mem_info['SwapTotal'][0])
        time.sleep(0.100)

if __name__ == "__main__":
    # execute only if run as a script
    main()