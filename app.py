from flask import Flask, render_template, jsonify
import sensors  # Import sensor simulation

app = Flask(__name__)

# Routes to serve HTML pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control-device')
def control_device():
    return render_template('control-device.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/team')
def team():
    return render_template('team.html')

# Route to fetch sensor data
@app.route('/sensor-data')
def sensor_data():
    data = sensors.get_sensor_data()  # Get data from sensors.py
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
