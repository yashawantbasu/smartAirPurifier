import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
pin=27
GPIO.setup(pin, GPIO.OUT) 
GPIO.output(pin, GPIO.HIGH)
def getSystime():
    return time.strftime("%H:%M")
    
time1="13:17"
time2="13:18"

while True:
	if(getSystime()==time1):
            GPIO.output(pin,GPIO.LOW)
            print("Relay on")
        if(getSystime()==time2):
            GPIO.output(pin, GPIO.HIGH)
            print("Relay off")
	time.sleep(1)
