from util.stopwatch import stopwatch as SW
import os
import sys
from networktables import NetworkTables as NT
import socket
from collections import namedtuple

"""
telemetry push system 
"""

ROBOT = 'roborio-501-frc.local'  # set robot name
ROBOT_IP = socket.gethostbyname(ROBOT)  # determine robot IP

with open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq') as f:  # read CPU frequency
    cpu_freq = int(f.read())
f.closed

MHz = int(cpu_freq / 1000.0)
clock_speed = str(MHz) + ' MHz'
print(clock_speed)




MemInfoEntry = namedtuple('MemInfoEntry', ['value', 'unit'])  # gets memory information
mem_info = {}
with open('/proc/meminfo') as file:
    for line in file:
        key, value, *unit = line.strip().split()
        mem_info[key.rstrip(':')] = MemInfoEntry(value, unit)
free_memory = str(int(int(mem_info['MemFree'][0]) / 1000 )) + ' MB'

print(free_memory)
print(mem_info['SwapFree'][0])
print(mem_info['SwapTotal'][0])