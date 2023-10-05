# This program is to test connecting to the HC-O5 Bluetooth module.

import serial
import time

# defines the Serial port and automatically opens the serial connection
# Note: The port name must be changed depending on the pc using this program
# Note: The baudrate must match the HC-05's baudrate. As of now, the HC-05's baudrate is 38400
arduino = serial.Serial("COM11", baudrate=38400, timeout=1)

# sends a signal to the arduino via serial connection (USB)
def command(x):
    arduino.write(bytes(x,'utf-8'))
    # x = int(x)
    # x = bytes(x)
    # arduino.write(x)

    # byte_to_write = b'4'
    # arduino.write(byte_to_write)

# Reads user input and sends the number to the arduino
while(True):
    cmd = input("Type number (single-digit) you want to write via bluetooth: \n")
    command(cmd)
    time.sleep(1)

