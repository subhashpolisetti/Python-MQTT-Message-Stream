import paho.mqtt.client as mqtt
import time

# MQTT settings
broker = "localhost"  # Use 'localhost' if Mosquitto is running on your machine
port = 1883           # Default port for MQTT
topic = "test/topic"  # Topic to publish messages to

# Create a new MQTT client instance using the latest API
client = mqtt.Client(protocol=mqtt.MQTTv5)  # Updated to MQTT version 5 for the latest standard

# Define callback for connection
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Connected to the broker successfully.")
    else:
        print("Failed to connect, return code %d\n", rc)

client.on_connect = on_connect

# Connect to the broker
client.connect(broker, port)

# Publish 1,000,000 messages
message_count = 1000000

for i in range(message_count):
    message = f"Message {i+1}"
    client.publish(topic, payload=message, qos=0)
    
    # Optional: Adjust this sleep time if messages are sent too fast for the subscriber to handle
    time.sleep(0.001)

print("Publishing complete!")

# Disconnect from the broker
client.disconnect()
