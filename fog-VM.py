from flask import Flask, request, redirect
import requests
import random

app = Flask(__name__)

CLOUD_URL = 'http://34.16.149.156:5000/remote'  # URL of Cloud VM

@app.route('/', methods=['GET'])
def home():
    # When the Fog server do not have enough computing resources or the task is heavy, Fog redirects request to the Cloud
    # Its calculated based on business logic.
    # Here we do not have real time date so we are simulating it using random function.
    computResReq = random.randint(1, 10) # Resources required to compute the task.
    heavyTsk = random.randint(1, 10) # Measure to check how heavy the task is.

    # Receive data from the GET request
    received_data = request.args.to_dict()

    # Checks if values of computResReq and heavyTsk are greater than threshold then redirects request to the Cloud.
    if computResReq > 5 or heavyTsk > 8.5:
        response = requests.get(CLOUD_URL , json=received_data) # Response received from Cloud which inturn is sent to the Broker.
        return response.text

    return "ACTION TAKEN BY FOG! {With low latency}"


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
