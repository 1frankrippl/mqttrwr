# mqttrwr server - rewrite mqtt topics
mqtt rewrite is a server written in python to connect to a mqtt broker to rewrite mqtt topics. This might be needed in the case you are connecting to a 3rd mqtt broker where you do not control the structure of topics (e.g. The Things Network). This server can be used to rewrite the topics in a structure you need. 

[![master](https://img.shields.io/badge/master-v3.0.2-blue.svg)](https://github.com/1frankrippl/mqttrwr/tree/master)

If you like **mqttrwr** give it a star or fork it:

[![GitHub stars](https://img.shields.io/github/stars/1frankrippl/mqttrwr.svg?style=social&label=Star)](https://github.com/1frankrippl/mqttrwr/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/1frankrippl/mqttrwr.svg?style=social&label=Fork)](https://github.com/1frankrippl/mqttrwr/network)

# Installation:
## Python prerequisites
If not already done, install Python 3.x environment with pip and paho MQTT.
```bash
sudo apt install python3 python3-pip python3-paho-mqtt
```
## install mqttrwr

1. Download config.yaml and mqtt_rewrite.py
2. Place both files into one folder
3. Configure the server in config.yaml
```yaml
  mqtt:
  broker: "<HOSTNAME>"
  port: 1883
  username: "username"
  password: "password"
topics:
  - sub_topic: "original/topicwithwildcard/#"
    pub_topic: "targettopic/2ndlevel"
  - sub_topic: "original/topicwithwildcard/#"
    pub_topic: "targettopic/2ndlevel"
  - sub_topic: "original2"
    pub_topic: "targettopic2/"
```
5. For testing you can start the service with
```bash
python mqtt_rewrite.py
```
# Setting up mqttrwr service 

On Linux you can run mqtt rewrite as a server 

```bash
sudo vi /etc/systemd/system/mqttrwr.service
```
```
Contents:
[Unit]
Description=MQTTrwr Server Script
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/your/mqtt_rewrite.py
WorkingDirectory=/path/to/your/
StandardOutput=inherit
StandardError=inherit
Restart=always
User=pi
Environment=PYTHONUNBUFFERED=1

[Install]
WantedBy=multi-user.target
```
```bash
sudo systemctl daemon-reload
```
```bash
sudo systemctl start mqttrwr.service 
sudo systemctl enable mqttrwr.service
```
```bash
sudo systemctl status mqttrwr.service
```

