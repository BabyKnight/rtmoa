import serial
import sys


"""
Defination of serial data
[m] - normal message
[a] - Accelerometer
[g] - Gyroscope
"""

DIRECTION = {
    0 : "UP",
    1 : "DOWN",
    2 : "RIGHT",
    3 : "LEFT",
    4 : "UNKNOWN",
        }


def get_direction(x, y, z):
    """
    Calculate the direction based on the Accelerometer
    Initial position to set Type C port in the bottom
    """
    var = {
        "X": x,
        "Y": y,
        "Z": z
        }

    max_var_axis = max(var, key=lambda k: abs(var[k]))
    max_var_val = var[max_var_axis]
    print(max_var_axis + str(max_var_val))
    if max_var_axis is "X" and max_var_val > 0:
        return 0
    elif max_var_axis is "X" and max_var_val < 0:
        return 1
    elif max_var_axis is "Y" and max_var_val > 0:
        return 2
    elif max_var_axis is "Y" and max_var_val < 0:
        return 3
    else:
        return 4


def monitor_orientation_adjustment():
    """
    """
    pass


def process_sensor_data(raw_data):
    """
    Process the raw sensor data and decided if monitor orientation adjustment needed
    """
    if raw_data.startswith("[a]"):
        data = raw_data[3:].split(",")
        if len(data) == 3:
            x, y, z = map(float, data)
            print(x, y, z)
            direction = get_direction(x, y, z)
            print(DIRECTION[direction])


def read_serial_data():
    """
    Read sensor data from serial port and process the parsed values.
    """
    ser = serial.Serial('/dev/ttyACM0', 9600)

    print("Waiting for data...")

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            #print(line)
            process_sensor_data(line)


if __name__ == '__main__':
    read_serial_data()
    sys.exit(0)

