import random
import time
from datetime import datetime


# Custom Exception for Sensor Errors
class SensorError(Exception):
    def __init__(self, message):
        super().__init__(message)


# Base Sensor Class
class Sensor:
    def __init__(self, location):
        self.location = location
        self.last_checked = None

    def read_data(self):
        raise NotImplementedError("Subclasses must implement this method.")


# Temperature Sensor Class
class TemperatureSensor(Sensor):
    def read_data(self):
        self.last_checked = datetime.now()
        temperature = random.uniform(20.0, 100.0)  # Random temp in Celsius
        if random.random() < 0.05:
            raise SensorError(f"Temperature sensor failure at {self.location}")
        return round(temperature, 2)


# Smoke Sensor Class
class SmokeSensor(Sensor):
    def read_data(self):
        self.last_checked = datetime.now()
        smoke_level = random.randint(0, 10)  # 0 = clear, 10 = thick smoke
        if random.random() < 0.05:
            raise SensorError(f"Smoke sensor failure at {self.location}")
        return smoke_level


# Monitor Station for Handling Multiple Sensors
class MonitorStation:
    def __init__(self, station_id):
        self.station_id = station_id
        self.temperature_sensors = []
        self.smoke_sensors = []
        self.logs = []

    def add_temperature_sensor(self, location):
        self.temperature_sensors.append(TemperatureSensor(location))

    def add_smoke_sensor(self, location):
        self.smoke_sensors.append(SmokeSensor(location))

    def run_diagnostics(self):
        print(f"\nRunning diagnostics for Station {self.station_id}...\n")
        for sensor in self.temperature_sensors + self.smoke_sensors:
            try:
                reading = sensor.read_data()
                status = f"{sensor.__class__.__name__} at {sensor.location} reading: {reading}"
                self.logs.append((sensor.location, datetime.now(), reading))
                print(status)
            except SensorError as e:
                self.logs.append((sensor.location, datetime.now(), "ERROR"))
                print(f"ERROR: {e}")

    def detect_wildfire(self):
        alert = False
        print("\nEvaluating wildfire conditions...\n")
        for t_sensor, s_sensor in zip(self.temperature_sensors, self.smoke_sensors):
            try:
                temp = t_sensor.read_data()
                smoke = s_sensor.read_data()
                print(f"[{t_sensor.location}] Temp: {temp}°C, Smoke: {smoke}")
                if temp > 50 and smoke >= 7:
                    print(f"🔥 Wildfire Alert at {t_sensor.location}! 🔥")
                    alert = True
            except SensorError as e:
                print(f"Sensor error: {e}")
        return alert

    def save_logs(self, filename="wildfire_logs.txt"):
        with open(filename, "a") as f:
            for log in self.logs:
                f.write(f"{log[0]} | {log[1]} | {log[2]}\n")
        print("\nLogs saved successfully.\n")


# Utility function to simulate user interface
def main_menu():
    print("\n Wildfire Monitoring Interface ")
    print("1. Run Diagnostics")
    print("2. Detect Wildfire")
    print("3. Save Logs")
    print("4. Exit\n")


# Driver code
def main():
    station = MonitorStation("PA-001")
    locations = ["Forest A", "Hilltop", "Lakeview", "East Ridge"]

    # Add sensors (assuming 1 of each type per location)
    for loc in locations:
        station.add_temperature_sensor(loc)
        station.add_smoke_sensor(loc)

    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            station.run_diagnostics()
        elif choice == "2":
            wildfire = station.detect_wildfire()
            if not wildfire:
                print("\nNo wildfire detected at this time.\n")
        elif choice == "3":
            station.save_logs()
        elif choice == "4":
            print("\nExiting the monitoring system. Stay safe!\n")
            break
        else:
            print("\nInvalid choice. Please try again.\n")
        time.sleep(1)


if __name__ == "__main__":
    main()

