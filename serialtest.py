import serial
import serial.tools.list_ports
import time

# Find available serial ports
ports = list(serial.tools.list_ports.comports())
if not ports:
    print("No serial ports found. Make sure your Arduino is connected.")
    exit()

# Use the first available port (you may want to add more logic to choose the correct port)
arduino_port = ports[0].device

# Define the Serial port and automatically open the serial connection
arduino = serial.Serial(arduino_port, baudrate=9600, timeout=1)

# Sends a signal to the Arduino via serial connection (USB)
def command(x):
    arduino.write(bytes(x, 'utf-8'))

# Reads user input and sends the number to the Arduino
while True:
    cmd = input("Type 1 to open the box. Type 0 to close the box.\n")
    command(cmd)
    time.sleep(1)
