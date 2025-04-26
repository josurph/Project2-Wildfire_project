from flask import Flask, render_template, jsonify
import random
import time
from threading import Thread

app = Flask(__name__)

sensor_data = {
    "temperature": 25.0,
    "smoke": 0.0,
    "fire_detected": False
}
def simulate_sensor_data():
    while True:
        temp = random.uniform(20, 50)      
        smoke = random.uniform(0, 100)     
        fire = temp > 45 and smoke > 70    

        sensor_data.update({
            "temperature": round(temp, 2),
            "smoke": round(smoke, 2),
            "fire_detected": fire
        })

        time.sleep(2)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/data")
def api_data():
    return jsonify(sensor_data)

if __name__ == "__main__":
    Thread(target=simulate_sensor_data, daemon=True).start()
    app.run(debug=True)

