import serial
import time

# defines the Serial port and automatically opens the serial connection
arduino = serial.Serial("COM9", baudrate=9600, timeout=1) # Edit the name of the com port
print("Hello")

# sends a signal to the arduino via serial connection (USB)
def command(x):
    arduino.write(bytes(x,'utf-8'))

# Reads user input and sends the number to the arduino
while(True):
    cmd = input("Type 1 to open the box. Type 0 to close the box.\n")
    command(cmd)
    time.sleep(1)

