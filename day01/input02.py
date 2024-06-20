# 키보드 입력으로 led 제어
import RPi.GPIO as GPIO
import time
 
led1 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)

try:
	while True:
		x = input('o 켜기 x 끄기')
		if(x == 'o'):
			GPIO.output(led1, False)
		elif(x == 'x'):
			GPIO.output(led1, True)
			
except KeyboardInterrupt:  #Ctrl + c
    GPIO.cleanup()
