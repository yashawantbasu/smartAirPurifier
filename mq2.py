import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
sensor=27
GPIO.setup(sensor,GPIO.IN)
while True:
	if(GPIO.input(sensor)==True):
		print("smoke")
	else:
		print("no smoke")
		
	print("\n")
	time.sleep(1);

