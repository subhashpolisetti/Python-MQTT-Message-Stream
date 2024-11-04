import paho.mqtt.client as mqtt

# MQTT settings
broker = "localhost"
port = 1883
topic = "test/topic"

# Initialize message counter
message_count = 0

# Callback function for when a message is received
def on_message(client, userdata, message):
    global message_count
    message_count += 1
    
    # Print count every 10,000 messages to monitor progress
    if message_count % 10000 == 0:
        print(f"Received {message_count} messages")

# Create MQTT client instance
client = mqtt.Client()

# Assign callback function
client.on_message = on_message

# Connect to the broker
client.connect(broker, port)

# Subscribe to the topic
client.subscribe(topic)

# Start the loop to process received messages
print("Subscriber is running and waiting for messages...")
client.loop_forever()
