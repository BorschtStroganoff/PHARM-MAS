# This program was used in testing the servo motors to be used in the EPICS PHARM MAS project.
# It uses a serial connection to the arduino via the PySerial library.
# To use this program, you have to install the PySerial libary (https://pypi.org/project/pyserial/)
# Essentially, you have to type "pip install pyserial" into a command terminal, either from vscode's terminal or thru cmd.exe running as administrator

import serial
import time

# defines the Serial port and automatically opens the serial connection
arduino = serial.Serial("COM9", baudrate=9600, timeout=1) # Edit the name of the com port

# sends a signal to the arduino via serial connection (USB)
def command(x):
    arduino.write(bytes(x,'utf-8'))

# Reads user input and sends the number to the arduino
while(True):
    cmd = input("Type 1 to open the box. Type 0 to close the box.\n")
    command(cmd)
    time.sleep(1)

