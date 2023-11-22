from flask import Flask, request

app = Flask(__name__)

# When the request comes directly from broker to Cloud.
@app.route('/', methods=['GET'])
def home():
    # Business logic performed.
    # Suitable action taken and response send to Broker
    return "REQUEST FROM BROKER : ACTION TAKEN FROM CLOUD {Moderate latency}"

# When the request comes from Fog to Cloud.
@app.route('/remote', methods=['GET'])
def remote():
    # Business logic performed.
    # Suitable action taken and response send to Fog
    received_data = request.args.to_dict()
    return "REQUEST FROM FOG : DATA PROCESSED/ACTION TAKEN BY CLOUD! {High latency}"

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
