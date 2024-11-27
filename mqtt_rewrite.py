import paho.mqtt.client as mqtt
import yaml
import re

# Load configuration file
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

# MQTT broker information from the configuration
broker = config["mqtt"]["broker"]
port = config["mqtt"]["port"]
username = config["mqtt"]["username"]
password = config["mqtt"]["password"]

# Topics from the configuration
topics = config["topics"]

# Callback function for connection establishment
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    for topic in topics:
        client.subscribe(topic["sub_topic"])

# Callback function for incoming messages
def on_message(client, userdata, msg):
    print(f"Message received: {msg.payload.decode()} on topic: {msg.topic}")
    for topic in topics:
        if re.match(topic["sub_topic"].replace("+", "[^/]+").replace("#", ".+"), msg.topic):
            client.publish(topic["pub_topic"], msg.payload.decode())
            print(f"Message forwarded to topic: {topic['pub_topic']}")
            break

# Set up the MQTT client
client = mqtt.Client()
client.username_pw_set(username, password)
client.on_connect = on_connect
client.on_message = on_message

# Establish connection to the broker
client.connect(broker, port, 60)

# Start the MQTT loop
client.loop_forever()
