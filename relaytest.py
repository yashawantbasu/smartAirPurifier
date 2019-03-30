import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
pin=27
GPIO.setup(pin, GPIO.OUT) 
GPIO.output(pin, GPIO.LOW)
while True:
	GPIO.output(pin,GPIO.HIGH)
	print("Relay off")
	time.sleep(10)
	GPIO.output(pin, GPIO.LOW)
	print("Relay on")
	time.sleep(10)

#GPIO.cleanup()