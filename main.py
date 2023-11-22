from flask import Flask

import tkinter as tk
from tkinter import PhotoImage , font
import random
import requests


FOG_VM_URL = 'http://34.131.53.159:5000/'
CLOUD_VM_URL = "http://34.16.149.156:5000/"

def simulate_sensor(sensor_id, sensor_type):

    data = {
        "sensor_id": sensor_id,
        "sensor_type": sensor_type,
        "value": round(random.uniform(20.0, 30.0), 2),
        "priority": round(random.uniform(0, 10), 2),
        "critical": round(random.uniform(0, 10), 2)
    }
    return data



app = Flask(__name__)

def broker(data):
    if should_forward_to_fog(data):
        forward_data_to_fog(data)
        return 'Data forwarded to Fog VM'
    else:
        forward_data_to_cloud(data)
        return 'Data forwarded to Cloud VM'

def should_forward_to_fog(data):
    if data['priority'] > 5 and data['critical'] < 7.8 :
        return True
    else:
        return False

def forward_data_to_fog(data):
    print("forwarding to fog computer..")
    fog_response = requests.get(FOG_VM_URL, json=data)
    print(f"FOG Computer responded: {fog_response.text}")
    fogText = tk.Label(root, text=fog_response.text
                     ,bg="white")
    fogText.grid(row=2, column=2, rowspan=4, padx=(220, 0), pady=(0, 0))
    root.after(3000, lambda: fogText.destroy())

def forward_data_to_cloud(data):
    print("forwarding to cloud computer..")
    cloud_response = requests.get(CLOUD_VM_URL, json=data)
    cloudText = tk.Label(root, text=cloud_response.text
                     ,bg="white")
    cloudText.grid(row=0, column=2, rowspan=2, padx=(180, 0), pady=(130, 0))
    print(f"CLOUD Computer responded: {cloud_response.text}")
    root.after(3000, lambda: cloudText.destroy())




def on_button_click(button_number):
    data = simulate_sensor(button_number, "IOT")
    label = tk.Label(root, text=f"SENSOR {data['sensor_id']} DATA GENERATED: \n Priority: {data['priority']} "
                                f"Criticality: {data['critical']}"
                     , bg="white" , font=font.Font(weight='bold'))
    label.grid(row=0, column=2, rowspan=4, padx=(10, 0), pady=(10, 0))
    broker(data)


root = tk.Tk()
root.title("Broker pattern FOG Computing")
root.attributes('-fullscreen', True)


root.configure(bg="white")

sensor_button_image = PhotoImage(file="img.png")

resized_sensor_button_image = sensor_button_image.subsample(3, 3)


sensor1 = tk.Button(root, image=resized_sensor_button_image, command=lambda: on_button_click(1), bd=0, bg="white")
sensor2 = tk.Button(root, image=resized_sensor_button_image, command=lambda: on_button_click(2), bd=0, bg="white")
sensor3 = tk.Button(root, image=resized_sensor_button_image, command=lambda: on_button_click(3), bd=0, bg="white")
sensor4 = tk.Button(root, image=resized_sensor_button_image, command=lambda: on_button_click(4), bd=0, bg="white")


sensor1.grid(row=0, column=0, sticky="w", padx=(30, 0), pady=(60, 0))
sensor2.grid(row=1, column=0, sticky="w", padx=(30, 0), pady=(20, 0))
sensor3.grid(row=2, column=0, sticky="w", padx=(30, 0), pady=(20, 0))
sensor4.grid(row=3, column=0, sticky="w", padx=(30, 0), pady=(20, 0))


broker_image = PhotoImage(file="broker.png")
broker_image_label = tk.Label(root, image=broker_image, bg="white")
broker_image_label.grid(row=0, column=1, rowspan=4, padx=(200, 0), pady=(20, 0))


cloud_image = PhotoImage(file="cloud.png")
cloud_image_label = tk.Label(root, image=cloud_image, bg="white")
cloud_image_label.grid(row=0, column=2, sticky="ne", padx=(200, 0), pady=(20, 0))


line_bf_image = PhotoImage(file="arrow1.png")
resized_bf_line_image = line_bf_image.subsample(2, 2)
line_bf_image_label = tk.Label(root, image=resized_bf_line_image, bg="white")
line_bf_image_label.grid(row=2, column=2, sticky="ne", padx=(00, 300), pady=(170, 0))


line_bc_image = PhotoImage(file="arrow2.png")
resized_bc_line_image = line_bc_image.subsample(2, 2)
line_bc_image_label = tk.Label(root, image=resized_bc_line_image, bg="white")
line_bc_image_label.grid(row=0, column=2, sticky="ne", padx=(00, 390), pady=(140, 0))




fog_image = PhotoImage(file="img_1.png")
resized_fog_image = fog_image.subsample(2, 2)

fog_image_label = tk.Label(root, image=resized_fog_image, bg="white")
fog_image_label.grid(row=3, column=2, sticky="se", padx=(100, 20), pady=(0, 20))


root.mainloop()

