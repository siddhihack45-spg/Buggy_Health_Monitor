
class SensorData:
    def __init__(self, engine_temp, vibration, suspension):
        self.engine_temp = engine_temp
        self.vibration = vibration
        self.suspension = suspension

    def get_readings(self):
        return [
            self.engine_temp,
            self.vibration,
            self.suspension
        ]

    def display(self):
        print("\n--- BUGGY SENSOR READINGS ---")
        print("Engine temperature:", self.engine_temp)
        print("Vibration:", self.vibration)
        print("Suspension:", self.suspension)