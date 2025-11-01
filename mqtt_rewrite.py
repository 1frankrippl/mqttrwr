import paho.mqtt.client as mqtt
import yaml
import json
import re
import sys
from parsers import get_parser

with open("config.yaml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)

mqtt_in_cfg = cfg["mqtt_in"]
mqtt_out_cfg = cfg["mqtt_out"]
rewrite_rules = cfg["rewrite_rules"]

def on_connect(client, userdata, flags, rc):
    print(f"[MQTT] Verbunden mit Code {rc}")
    for rule in rewrite_rules:
        print(f"[MQTT] Abonniere: {rule['from']}")
        client.subscribe(rule["from"])

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode("utf-8")
    print(f"[MQTT] Empfangen: {topic} → {payload}")

    for rule in rewrite_rules:
        pattern = "^" + re.sub(r"\+", "([^/]+)", rule["from"]) + "$"
        match = re.match(pattern, topic)
        if match:
            groups = match.groups()
            new_topic = rule["to"]
            for g in groups:
                new_topic = new_topic.replace("+", g, 1)

            parser_name = rule.get("parser")
            if parser_name:
                try:
                    json_payload = json.loads(payload)
                    parser_func = get_parser(parser_name)
                    parsed = parser_func(json_payload)
                    payload = json.dumps(parsed)
                except Exception as e:
                    print(f"[Parser:{parser_name}] Fehler: {e}")

            print(f"[MQTT] Weiterleiten: {new_topic} → {payload}")
            mqtt_out.publish(new_topic, payload)
            break

mqtt_in = mqtt.Client()
mqtt_in.username_pw_set(mqtt_in_cfg["username"], mqtt_in_cfg["password"])
mqtt_in.on_connect = on_connect
mqtt_in.on_message = on_message
mqtt_in.connect(mqtt_in_cfg["host"], mqtt_in_cfg["port"], 60)

mqtt_out = mqtt.Client()
mqtt_out.username_pw_set(mqtt_out_cfg["username"], mqtt_out_cfg["password"])
mqtt_out.connect(mqtt_out_cfg["host"], mqtt_out_cfg["port"], 60)

try:
    mqtt_in.loop_forever()
except KeyboardInterrupt:
    print("\n[MQTT] Beende...")
    sys.exit(0)
