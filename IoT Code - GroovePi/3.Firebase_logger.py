from grovepi import *
from grove_rgb_lcd import *
from time import sleep
from math import isnan
import time
from time import strftime
from firebase import firebase
import math

dht_sensor_port = 7 # connect the DHt sensor to port 7
dht_sensor_type = 0 # use 0 for the blue-colored sensor and 1 for the white-colored se$
# set green as backlight color
setRGB(0,255,0)
#Host id is the data base URL
firebase= firebase.FirebaseApplication('https://fsiat-weather-monitoring.firebaseio.com/')
while True:
        try:
        # get the temperature and Humidity from the DHT sensor
                [ temp,hum ] = dht(dht_sensor_port,dht_sensor_type)
                print("temp =", temp, "C\thumidity =", hum,"%")
                location="Amrita,Bangalore"
		        time_stamp=strftime("%d-%m-%y %H:%M:%S", time.localtime()) #reads the machine time
                # check if we have nans
                # if so, then raise a type error exception
                if isnan(temp) is True or isnan(hum) is True:
                        raise TypeError('nan error')
                t = str(temp)
                h = str(hum)
                data={"Location":location,"time_stamp":time_stamp,"Temperature":temp,"Humidity":hum}
		        print(data)
		        result=firebase.post('Weather Station', data)
		        print(result)
setText_norefresh("Temp:" + t + "C\n" + "Humidity :" + h + "%")
        except (IOError, TypeError) as e:
                print(str(e))
                # and since we got a type error
                # then reset the LCD's text
                setText("")
        except KeyboardInterrupt as e:
                print(str(e))
                # since we're exiting the program
                # it's better to leave the LCD with a blank text
                setText("")
                break
# wait some time before re-updating the LCD
        sleep(0.05)
