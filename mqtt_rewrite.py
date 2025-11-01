import yaml
import paho.mqtt.client as mqtt
import json
import re

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    for topic in config["topics"]:
        client.subscribe(topic["sub_topic"])

def parse_payload(payload, parser_config):
    if parser_config["type"] == "json":
        try:
            data = json.loads(payload)
            return data.get(parser_config["key"], None)
        except json.JSONDecodeError:
            return None
    elif parser_config["type"] == "regex":
        match = re.search(parser_config["pattern"], payload)
        return match.group(1) if match else None
    else:
        return payload  # fallback: no parsing

def on_message(client, userdata, msg):
    for topic_cfg in config["topics"]:
        if mqtt.topic_matches_sub(topic_cfg["sub_topic"], msg.topic):
            payload = msg.payload.decode("utf-8")
            parser = topic_cfg.get("parser")
            if parser:
                parsed_value = parse_payload(payload, parser)
                if parsed_value is not None:
                    client.publish(topic_cfg["pub_topic"], str(parsed_value))
            else:
                client.publish(topic_cfg["pub_topic"], payload)

client.on_connect = on_connect
client.on_message = on_message

client.connect(config["broker"]["host"], config["broker"]["port"], 60)
client.loop_forever()
