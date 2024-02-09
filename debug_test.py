import tkinter as tk
from tkinter import simpledialog, messagebox
import serial
import serial.tools.list_ports
import time
import subprocess

def light_on(serial_port='/dev/ttyACM0', baud_rate=9600):
    try:
        ser = serial.Serial(serial_port, baud_rate)
        time.sleep(2) 
        ser.write(b'1')
        print("Sent '1' to Arduino")
        ser.close()
    except Exception as e:
        print(f"Failed to send data to Arduino: {e}")

def light_off(serial_port='/dev/ttyACM0', baud_rate=9600):
    try:
        ser = serial.Serial(serial_port, baud_rate)
        time.sleep(2) 
        ser.write(b'0')
        print("Sent '1' to Arduino")
        ser.close()
    except Exception as e:
        print(f"Failed to send data to Arduino: {e}")

def take_image():

def open_dr(serial_port='/dev/ttyACM0', baud_rate=9600):
    try:
        ser = serial.Serial(serial_port, baud_rate)
        time.sleep(2) 
        ser.write(b'2')
        print("Sent '1' to Arduino")
        ser.close()
    except Exception as e:
        print(f"Failed to send data to Arduino: {e}")
        
if __name__ == "__main__":
    root = tk.Tk()

    bt_light_on = tk.Button(root, text="Set Number of Compartments", command=light_on)
    bt_light_on.pack(pady=10)

    bt_light_off = tk.Button(root, text="Set Maximum Items", command=light_off)
    bt_light_off.pack(pady=10)

    bt_take_image = tk.Button(root, text="Store", command=take_image)
    bt_take_image.pack(pady=10)

    bt_open_dr = tk.Button(root, text="Retrieve", command=open_dr)
    bt_open_dr.pack(pady=10)

    root.mainloop()
