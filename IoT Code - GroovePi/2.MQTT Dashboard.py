#pip install paho-mqtt
# Might not work for python 3(Use Python 2)
import paho.mqtt.client as mqtt
from grovepi import *
import time

led = 7

pinMode(led,"OUTPUT")

def on_connect(client, userdata, flags, rc):
    print("Connected to broker. Return of connection: "+str(rc))

    client.subscribe("/MQTTLED/#")

# Callback - when a message is received
def on_message(client, userdata, msg):
        print("Topic: "+msg.topic+" - Message Received: "+str(msg.payload))

        if (str(msg.payload) == "ONLED1"):
          digitalWrite(led,True)
          return 0

        if (str(msg.payload) == "OFFLED1"):
          digitalWrite(led,False)
          return 0

#main program
client = mqtt.Client()
client.on_connect = on_connect   # configure callback (from when the connection$
client.on_message = on_message   # set callback (from when a message is receive$

client.connect("test.mosquitto.org", 1883, 60)

# Endless loop waiting to receive messages. .
client.loop_forever()
