# This program is to test connecting to the HC-O5 Bluetooth module.

import serial
import time

# defines the Serial port and automatically opens the serial connection
# Note: The port name must be changed depending on the pc using this program
# Note: The baudrate must match the HC-05's baudrate. As of now, the HC-05's baudrate is 38400
arduino = serial.Serial("COM11", baudrate=38400, timeout=1)

# sends a signal to the arduino via serial connection (USB)
def send(string):
    string += '\n'
    arduino.write(bytes(string,'utf-8'))

def read():

    while (arduino.in_waiting <= 0):
        pass

    data_from_arduino = arduino.read_until(b'\n')
    string_from_arduino = data_from_arduino.decode('utf-8').strip()

    return string_from_arduino


    
# Reads user input and sends the number to the arduino
while(True):
    message_to_arduino = input("Type message you want to write via bluetooth: ")
    send(message_to_arduino)

    message_from_arduino = read()
    print(f"Message from arduino: \"{message_from_arduino}\"")
    time.sleep(1)

