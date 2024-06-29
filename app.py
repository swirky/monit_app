from flask import Flask,render_template, jsonify
import json,random
import datetime
from collections import deque
from simulations import Simulations

app = Flask(__name__)

# Przechowywanie ostatnich 10 wartości temperatury, wilgotności i dat
data_history = deque(maxlen=10)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def api_data():
    temperature1 = Simulations.get_temp_sensor1()
    temperature2 = Simulations.get_temp_sensor2()
    humidity = Simulations.get_humidity()
    current_datetime = Simulations.get_current_datetime()
    data_history.append({
        'temperature1': temperature1,
        'temperature2': temperature2,
        'humidity': humidity,
        'datetime': current_datetime
    })
    data = {
        'temperature1': temperature1,
        'temperature2': temperature2,
        'humidity': humidity,
        'current_datetime': current_datetime
    }
    return jsonify(data)



@app.route('/wykresy', methods=["GET", "POST"])
def charts():
    labels = [entry['datetime'] for entry in data_history]
    data = [entry['temperature1'] for entry in data_history]
 
    
    return render_template('charts.html',data=data, labels=labels)

@app.route('/tabele', methods=["GET", "POST"])
def tables():
    return render_template('tables.html', data_history=data_history)

@app.route('/alerty', methods=["GET", "POST"])
def alerts():
    return render_template('alerts.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)