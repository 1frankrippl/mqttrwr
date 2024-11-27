# mqttrwr
mqtt rewrite is a server written in python to connect to a mqtt broker to rewrite mqtt topics in case you connect to a 3rd mqtt broker where you do not control the structure of topics (e.g. The Things Network). 

# Installation:
1. Download config.yaml and mqtt_rewrite.py
2. Place both files into one folder
3. For testing you can start the service with python mqtt_rewrite.py

# Setting up service 

On Linux you can run mqtt rewrite as a server 

1. Create Service
sudo vi /etc/systemd/system/mqttrwr.service

2.
