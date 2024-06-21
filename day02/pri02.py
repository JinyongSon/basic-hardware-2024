import RPi.GPIO as GPIO
import time

led1 = 21
pirPin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(pirPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.input(pirPin) == False

try:
	while True:
		if GPIO.input(pirPin) == True:
			GPIO.output(led1, False)
			print("Detected")
			time.sleep(1)
		else:
			GPIO.output(led1, True)
			print("undetected")
			time.sleep(1)

except:
	GPIO.cleanup()


