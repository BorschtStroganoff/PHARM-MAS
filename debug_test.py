# This is the code used on the raspberry pi 4b for debugging purposed. We are making sure that all the software and hardware work well in tandem

# Here are the installation commands that need to be sent to bash before this can be run:

# sudo apt-get update
# sudo apt-get install python3-pip libopenblas-base libopenblas-dev
# pip3 install torch torchvision pillow
# sudo apt-get install fswebcam
# sudo apt-get install python3-tk
# pip3 install Pillow


# Make sure that you have yolov5 installed, with the required weight file (ending in .pt) and detect.py in the same folder
# git clone https://github.com/ultralytics/yolov5.git


import tkinter as tk
from PIL import Image, ImageTk
import serial
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

def take_image():
    # Capture image
    subprocess.run(["fswebcam", "-r", "1920x1080", "--no-banner", "captured_image.jpg"])

    # YOLOv5 detection
    detect_script = "yolov5/detect.py"
    weight_file = "pencil.pt"
    image_file = "captured_image.jpg"

    detect_script = str(Path(__file__).resolve().parent / detect_script)
    weight_file = str(Path(__file__).resolve().parent / weight_file)
    image_file = str(Path(__file__).resolve().parent / image_file)

    if not (os.path.exists(detect_script) and os.path.exists(weight_file) and os.path.exists(image_file)):
        print("Error: YOLOv5 script, weight file, or image file not found.")
        return

    # Specify the output directory for YOLOv5 results
    output_dir = "inference/output"
    os.makedirs(output_dir, exist_ok=True)

    # Run YOLOv5 detection with the specified output directory
    detection_command = [
        "python3",
        detect_script,
        "--weights", weight_file,
        "--img-size", "640",
        "--conf", "0.25",
        "--source", image_file,
        "--save-txt",  # Save results in the output directory
        "--project", output_dir  # Specify the output directory
    ]

    subprocess.run(detection_command)

    # Load the result of YOLOv5 detection
    results_file = Path(output_dir) / "captured_image.jpg"
    if results_file.exists():
        image_result = Image.open(results_file)

        # Display the marked image in a new window
        result_window = tk.Toplevel(root)
        result_window.title("YOLOv5 Result")

        tk_image = ImageTk.PhotoImage(image_result)
        label = tk.Label(result_window, image=tk_image)
        label.pack(pady=10)

        # Process YOLOv5 results
        yolo_results = []
        with open(results_file.with_suffix(".txt"), "r") as result_file:
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

    # Set button size
    button_width = 15
    button_height = 5

    bt_light_on = tk.Button(root, text="Turn Light On", command=lambda: light_on(), width=button_width, height=button_height)
    bt_light_on.pack(pady=10)

    bt_light_off = tk.Button(root, text="Turn Light Off", command=lambda: light_off(), width=button_width, height=button_height)
    bt_light_off.pack(pady=10)

    bt_take_image = tk.Button(root, text="Take and Evaluate Image", command=take_image, width=button_width, height=button_height)
    bt_take_image.pack(pady=10)

    bt_open_drawer = tk.Button(root, text="Open Drawer", command=lambda: open_drawer(), width=button_width, height=button_height)
    bt_open_drawer.pack(pady=10)

    root.mainloop()


