from networktables import NetworkTables as NT
import socket
from collections import namedtuple
import time

"""
Telemetry Push Subsystem 
****
ONLY WORKS ON LINUX
****
Provides the following information to the Driver Station:
- SOC Temperature (thermal_zone0)
- CPU Frequency
- Free Memory
"""


sleep_time = 0.200  # time to wait between sending updates


def main():
    table = telemetry_init()
    telemetry_run(table)


def telemetry_init():
    ROBOT = 'roborio-501-frc.local'  # set robot name
    ROBOT_IP = socket.gethostbyname(ROBOT)  # determine robot IP
    nt_init = False

    while not nt_init:
        try:
            NT.initialize(server=ROBOT_IP)  # initialize client
        except:
            continue
        try:
            vision_table = NT.getTable('SmartDashboard')
        except:
            NT.stop()
            NT.destroy()
            continue
        vision_table.putBoolean('connected', True)
        pullback = vision_table.getBoolean('connected', None)
        if pullback:
            nt_init = True
        else:
            continue
    else:
        return vision_table

def telemetry_run(vision_table):
    while(True):
        with open('/sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq') as f:  # read CPU frequency
            cpu_freq = int(f.read())
        f.closed
        MHz = int(cpu_freq / 1000.0)
        clock_speed = str(MHz) + ' MHz'
        print(clock_speed)
        vision_table.putString('RPI/clock_speed', clock_speed)

        with open('/sys/class/thermal/thermal_zone0/temp') as f:  # read SOC temperature
            soc_temp = int(f.read())
        f.closed
        soc_temp = str(int(soc_temp / 1000)) + ' C'
        print(soc_temp)
        vision_table.putString('RPI/soc_temp', soc_temp)

        MemInfoEntry = namedtuple('MemInfoEntry', ['value', 'unit'])  # gets memory information
        mem_info = {}
        with open('/proc/meminfo') as file:
            for line in file:
                key, value, *unit = line.strip().split()
                mem_info[key.rstrip(':')] = MemInfoEntry(value, unit)
        free_memory = str(int(int(mem_info['MemFree'][0]) / 1000 )) + ' MB'
        print(free_memory)
        vision_table.putString('RPI/free_memory', free_memory)


        # print(mem_info['SwapFree'][0])
        # print(mem_info['SwapTotal'][0])
        time.sleep(sleep_time)

if __name__ == "__main__":
    # execute only if run as a script
    main()