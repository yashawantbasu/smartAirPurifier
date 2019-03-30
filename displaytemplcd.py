import RPi.GPIO as GPIO
import dht11
import time
import datetime
import sys
import os
import serial
#import serialget
sys.path.append('/home/pi/proj/Adafruit_CharLCD')
from Adafruit_CharLCD import Adafruit_CharLCD

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
lcd = Adafruit_CharLCD(rs=26, en=19,
                       d4=13, d5=6, d6=5, d7=11,
                       cols=16, lines=2)
ser = serial.Serial(              
               port='/dev/ttyACM0',
               baudrate = 9600,
               parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE,
               bytesize=serial.EIGHTBITS,
               timeout=1
           )
counter=0
def get_x():
        y=ser.readline()
        #x=y.decode("utf-8")
        #print(type(x))
        #print(x)
        #time.sleep(1)
        return y
lcd.clear()
# read data using pin 17
instance = dht11.DHT11(pin=17)
#y=ser.readline()
while True:
    result = instance.read()
    if result.is_valid():
	
	temp=result.temperature
	hum=result.humidity
	co_val=int(ser.readline()[:-2])
	aqi=12

	fin_message_line1="Temp:{0:0.1f}".format(temp)+" CO:"+str(co_val)
	fin_message_line2="Hum:{0:0.1f}".format(hum)+" AQI:"+str(aqi)
	
	print(fin_message_line1)
	print(fin_message_line2)

	lcd.clear()
	lcd.message(fin_message_line1+"\n"+fin_message_line2)

    time.sleep(1)



        
    
    
