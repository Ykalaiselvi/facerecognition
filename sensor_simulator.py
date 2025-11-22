# sensor_simulator.py
import time, json, random
import paho.mqtt.client as mqtt

BROKER = "test.mosquitto.org"   # public broker for demo; replace with your broker
PORT = 8000

TOPIC = "site1/water/sensors"

client = mqtt.Client("sensor_sim")
client.connect(BROKER, PORT, 60)
client.loop_start()

try:
    while True:
        data = {
            "ts": int(time.time()*1000),
            "ph": round(random.uniform(6.5, 8.5), 2),
            "turbidity": round(random.uniform(1.0, 120.0), 2),  # NTU
            "flow_rate": round(random.uniform(0.0, 5.0), 2),     # L/s
            "level": round(random.uniform(0.0, 2.0), 2)          # meters
        }
        payload = json.dumps(data)
        client.publish(TOPIC, payload)
        print("Published:", payload)
        time.sleep(5)  # publish every 5s
except KeyboardInterrupt:
    client.loop_stop()
    client.disconnect()
    print("Stopped sensor simulator")
