import json
from datetime import datetime

import paho.mqtt.client as mqtt


BROKER_HOST = "localhost"
BROKER_PORT = 1883
TOPIC = "hydroficient/grandmarina/#"


def print_dashboard_header():
    print("=" * 60)
    print("  GRAND MARINA WATER MONITORING DASHBOARD")
    print(f"  Connected at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print_dashboard_header()
        client.subscribe(TOPIC)
    else:
        print(f"Failed to connect. Reason code: {reason_code}")


def on_message(client, userdata, message):
    payload_text = message.payload.decode("utf-8")

    try:
        reading = json.loads(payload_text)
    except json.JSONDecodeError:
        print("\nReceived a non-JSON message:")
        print(payload_text)
        return

    location = reading.get("location", "unknown-location")
    device_id = reading.get("device_id", "unknown-device")
    timestamp = reading.get("timestamp", "unknown-time")
    counter = reading.get("counter", "unknown")
    pressure_upstream = reading.get("pressure_upstream")
    pressure_downstream = reading.get("pressure_downstream")
    flow_rate = reading.get("flow_rate")

    if pressure_upstream is not None and pressure_downstream is not None:
        pressure_differential = round(pressure_upstream - pressure_downstream, 1)
    else:
        pressure_differential = "unknown"

    print("\n" + "─" * 40)
    print(f"  Location:  {location}")
    print(f"  Device ID: {device_id}")
    print(f"  Time:      {timestamp}")
    print(f"  Count:     #{counter}")
    print("─" * 40)
    print(f"  Pressure (upstream):    {pressure_upstream} PSI")
    print(f"  Pressure (downstream):  {pressure_downstream} PSI")
    print(f"  Flow rate:              {flow_rate} gal/min")
    print(f"  Pressure differential:  {pressure_differential} PSI")


def main():
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER_HOST, BROKER_PORT, keepalive=60)

    try:
        client.loop_forever()
    except KeyboardInterrupt:
        print("\nSubscriber stopped by user.")
        client.disconnect()


if __name__ == "__main__":
    main()
