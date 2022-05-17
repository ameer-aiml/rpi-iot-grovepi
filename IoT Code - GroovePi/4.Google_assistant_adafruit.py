import sys
import RPi.GPIO as GPIO
from Adafruit_IO import MQTTClient

from grovepi import *

led = 7
pinMode(led,"OUTPUT")

ADAFRUIT_IO_KEY = ''
ADAFRUIT_IO_USERNAME =''
FEED_ID = 'raspi'
def connected(client):
    print('Connected to Adafruit IO!  Listening for {0} changes...'.format(FEED_ID))
    client.subscribe(FEED_ID)
def disconnected(client):
    print('Disconnected from Adafruit IO!')
    sys.exit(1)
def message(client, feed_id, payload):
    print('Feed {0} received new value: {1}'.format(feed_id, payload))
    if payload == "1":
                print("Light ON")
                digitalWrite(led,1)
    if payload == "0":
                print("Light OFF")
                digitalWrite(led,0)
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message
client.connect()
client.loop_blocking()
