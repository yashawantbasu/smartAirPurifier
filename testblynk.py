import RPi.GPIO as GPIO
import dht11
import time
import datetime
import sys
import os
import serial
sys.path.append('/home/pi/proj/blynklibrarypython')
import BlynkLib
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
blynk = BlynkLib.Blynk('2c6909a5c93d433aa1baf7c0ce06c444')
ser.reset_input_buffer()
buzzer=23
relay=27
count=0
count1=0
GPIO.setup(buzzer,GPIO.OUT)
lcd.clear()
# read data using pin 17
instance = dht11.DHT11(pin=17)
#deg = u'\xb0'
#y=deg.encode('utf8')
GPIO.output(buzzer,GPIO.LOW)

while True:
    result = instance.read()
    if result.is_valid():
	
	temp=result.temperature
	hum=result.humidity
	time.sleep(2)
        vallist=ser.readline()[:-2]
	count+=1
	count1+=1
	txt=vallist.split(' ')

	try:
		co_val=float(txt[0])
	except:
		co_val=0.0
	try:
		aqi=float(txt[1])
	except:
		aqi=0.0
	

	fin_message_line1="Temp:"+ str(temp) + "C" +" CO:"+ str(co_val)
	fin_message_line2="Hum:"+str(hum)+ "%" + " CO2:"+str(aqi)

	print(fin_message_line1)
	print(fin_message_line2)

	blynk.virtual_write(2, '{:.2f}'.format(temp))
    	blynk.virtual_write(3, '{:.2f}'.format(hum))
	blynk.virtual_write(4,co_val)
    	blynk.virtual_write(5,aqi)

	lcd.clear()
	if(co_val> 9.00):
		lcd.clear()
		lcd.message("Warning!!!\nC0 > 9 ppm")
		GPIO.output(buzzer,GPIO.HIGH)
		time.sleep(2)
		lcd.clear()
		lcd.message(fin_message_line1+"\n"+fin_message_line2)
		
	else:	
		lcd.message(fin_message_line1+"\n"+fin_message_line2)
       	
	if(aqi>=900):
		lcd.clear()
		lcd.message("Warning!!!\nC02 > 900 ppm")
		GPIO.output(buzzer,GPIO.HIGH)
		time.sleep(2)
		lcd.clear()
		lcd.message(fin_message_line1+"\n"+fin_message_line2)
					
	else:	
		lcd.message(fin_message_line1+"\n"+fin_message_line2)
	if (count>10):
		GPIO.output(buzzer,GPIO.LOW)
		count=0
	if (count1>2):
		ser.reset_input_buffer()
		count1=0
	blynk.run()

    #time.sleep(1)        
    



        
    
    
