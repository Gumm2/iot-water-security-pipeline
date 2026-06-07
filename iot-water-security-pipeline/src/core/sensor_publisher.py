import json
import random
import time
from datetime import datetime, timezone

import paho.mqtt.client as mqtt


BROKER_HOST = "localhost"
BROKER_PORT = 1883
TOPIC = "hydroficient/grandmarina/sensors/main-building/readings"

DEVICE_ID = "GM-HYDROLOGIC-01"
LOCATION = "main-building"
PUBLISH_INTERVAL_SECONDS = 2


class WaterSensorMQTT:
    def __init__(self, device_id, location):
        self.device_id = device_id
        self.location = location
        self.counter = 0

    def generate_reading(self):
        self.counter += 1

        pressure_upstream = round(random.uniform(75, 90), 1)
        pressure_downstream = round(random.uniform(70, 85), 1)
        flow_rate = round(random.uniform(30, 50), 1)

        reading = {
            "device_id": self.device_id,
            "location": self.location,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "counter": self.counter,
            "pressure_upstream": pressure_upstream,
            "pressure_downstream": pressure_downstream,
            "flow_rate": flow_rate,
        }

        return reading


def main():
    sensor = WaterSensorMQTT(DEVICE_ID, LOCATION)

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.connect(BROKER_HOST, BROKER_PORT, keepalive=60)

    print(f"Starting device: {DEVICE_ID}")
    print(f"Location: {LOCATION}")
    print(f"Publishing to: {TOPIC}")
    print(f"Interval: {PUBLISH_INTERVAL_SECONDS} seconds")
    print("----------------------------------------")

    try:
        while True:
            reading = sensor.generate_reading()
            message = json.dumps(reading)

            client.publish(TOPIC, message)

            print(
                f"[{reading['counter']}] "
                f"Pressure: {reading['pressure_upstream']}/{reading['pressure_downstream']} PSI, "
                f"Flow: {reading['flow_rate']} gal/min"
            )

            time.sleep(PUBLISH_INTERVAL_SECONDS)

    except KeyboardInterrupt:
        print("\nPublisher stopped by user.")

    finally:
        client.disconnect()


if __name__ == "__main__":
    main()
