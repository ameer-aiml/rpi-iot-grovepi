import time
from grovepi import *

led = 7
pinMode(led,"OUTPUT")

while True:
  digitalWrite(led,1)
  time.sleep(1)
  digitalWrite(led,0)
  time.sleep(1)
