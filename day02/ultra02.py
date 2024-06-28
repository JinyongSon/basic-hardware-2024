# Ultra
import RPi.GPIO as GPIO
import time

def measure():
	GPIO.output(trigPin, True)	
	time.sleep(0.00001)
	GPIO.output(trigPin, False)
	start = time.time()			

	while GPIO.input(echoPin) == False:
		start = time.time()				
	while GPIO.input(echoPin) == True:	
		stop = time.time()				
	elapsed = stop - start				
	distance = (elapsed * 19000) / 2	
	
	return distance						

# 핀설정
piezoPin = 13
trigPin = 27
echoPin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(piezoPin, GPIO.OUT)

Buzz = GPIO.PWM(piezoPin, 440)

try:
	while True:
		distance = measure()
		print("Distance: %2.f cm" %distance)
		if distance <= 50:
			Buzz.start(50)
			delay = distance / 100
			time.sleep(delay)
			Buzz.stop()
			time.sleep(delay)
		else:
			Buzz.stop()
			time.sleep(0.1)

except KeyboardInterrupt:
	GPIO.cleanup()
