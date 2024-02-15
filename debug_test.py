import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk  # Import ImageTk from PIL
import serial
import serial.tools.list_ports
import time
import subprocess
import os
from pathlib import Path

def light_on(serial_port='/dev/ttyACM0', baud_rate=9600):
    try:
        ser = serial.Serial(serial_port, baud_rate)
        time.sleep(2)
        ser.write(b'1')
        print("Sent '1' to Arduino")
        ser.close()
    except Exception as e:
        print(f"Failed to send data to turn on light to Arduino: {e}")

def light_off(serial_port='/dev/ttyACM0', baud_rate=9600):
    try:
        ser = serial.Serial(serial_port, baud_rate)
        time.sleep(2)
        ser.write(b'0')
        print("Sent '0' to Arduino")
        ser.close()
    except Exception as e:
        print(f"Failed to send data to turn off light to Arduino: {e}")

def take_image(label):
    # Capture image
    subprocess.run(["fswebcam", "-r", "1920x1080", "--no-banner", "captured_image.jpg"])

    # YOLOv5 detection
    detect_script = "detect.py"
    weight_file = "weight.pt"
    image_file = "captured_image.jpg"

    if not (os.path.exists(detect_script) and os.path.exists(weight_file) and os.path.exists(image_file)):
        print("Error: YOLOv5 script, weight file, or image file not found.")
        return

    # Run YOLOv5 detection
    detection_command = [
        "python3",
        detect_script,
        "--weights", weight_file,
        "--img-size", "1920x1080",
        "--conf", "0.4",
        "--source", image_file
    ]

    subprocess.run(detection_command)

    # Load the result of YOLOv5 detection and display in Tkinter GUI
    results_path = Path("inference", "output")
    results_file = results_path / "captured_image.jpg"

    if results_file.exists():
        image_result = Image.open(results_file)
        tk_image = ImageTk.PhotoImage(image_result)
        label.config(image=tk_image)
        label.image = tk_image  # Keep a reference to avoid garbage collection

        # Process YOLOv5 results
        yolo_results = []
        with open(results_path / "captured_image.txt", "r") as result_file:
            lines = result_file.readlines()
            for line in lines:
                class_id, confidence, x_min, y_min, x_max, y_max = map(float, line.split())
                yolo_results.append({
                    "class_id": int(class_id),
                    "confidence": confidence,
                    "bbox": (x_min, y_min, x_max, y_max)
                })

        print("YOLOv5 Detection Results:")
        for result in yolo_results:
            print(f"Class: {result['class_id']}, Confidence: {result['confidence']:.2f}, Bbox: {result['bbox']}")

def open_drawer(serial_port='/dev/ttyACM0', baud_rate=9600):
    try:
        ser = serial.Serial(serial_port, baud_rate)
        time.sleep(2)
        ser.write(b'2')
        print("Sent '2' to Arduino")
        ser.close()
    except Exception as e:
        print(f"Failed to send data to open drawer to Arduino: {e}")

if __name__ == "__main__":
    root = tk.Tk()

    # Create a label to display the image
    image_label = tk.Label(root)
    image_label.pack(pady=10)

    bt_light_on = tk.Button(root, text="Turn Light On", command=lambda: light_on())
    bt_light_on.pack(pady=10)

    bt_light_off = tk.Button(root, text="Turn Light Off", command=lambda: light_off())
    bt_light_off.pack(pady=10)

    bt_take_image = tk.Button(root, text="Take and Evaluate Image", command=lambda: take_image(image_label))
    bt_take_image.pack(pady=10)

    bt_open_drawer = tk.Button(root, text="Open Drawer", command=lambda: open_drawer())
    bt_open_drawer.pack(pady=10)

    root.mainloop()
