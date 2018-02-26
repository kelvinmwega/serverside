# Purpose of this application:
#      MQTT to HTTP Adapter for Door and Power Monitoring Devices
# prepared for
#      Voltarent Engineering
# Author:
#      kelvin mwega <kmwega@gmail.com>


import socket
import paho.mqtt.client as mqtt
import sys
import time
import requests
import json
import datetime
import serverProc as proc
import tcpClient as tcpclient

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))

	client.subscribe("VNT/trdl/Data")

def on_message(client, userdata, msg):
    time = datetime.datetime.now()
    print "Topic: ", msg.topic+'\nMessage: '+str(msg.payload)+'\n'+str(time)
    tcpclient.processRaw(msg)


def on_publish(mqttc, obj, mid) :
     print "completed..."
     sys.exit()


if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect("198.100.30.116", 1883, 60)
        #client.connect("localhost", 1883, 60)
        client.loop_forever()
    except Exception as e:
        client.disconnect()
        raise
