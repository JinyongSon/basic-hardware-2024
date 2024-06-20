import RPi.GPIO as GPIO
import time

led1 = 21
led2 = 20
led3 = 16
switch = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)

GPIO.output(led1, True)
GPIO.output(led2, True)
GPIO.output(led3, True)

current_led = 2

try:
	while True:
			if GPIO.input(switch) == True:
				time.sleep(0.2)
				current_led = (current_led + 1) % 3

				if current_led == 0:
					GPIO.output(led1, False)
					GPIO.output(led2, True)
					GPIO.output(led3, True)
				elif current_led == 1:
					GPIO.output(led1, True)
					GPIO.output(led2, False)
					GPIO.output(led3, True)
				elif current_led == 2:
					GPIO.output(led1, True)
					GPIO.output(led2, True)
					GPIO.output(led3, False)
			
except KeyboardInterrupt:
	GPIO.cleanup()
