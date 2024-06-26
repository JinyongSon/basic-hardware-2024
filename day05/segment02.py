import RPi.GPIO as GPIO
import time

segments = (21, 22, 23, 24, 25, 26, 27)
switch = 19
current_num = 0

num = [
    (1,1,1,1,1,1,0),  # 0
    (0,1,1,0,0,0,0),  # 1
    (1,1,0,1,1,0,1),  # 2
    (1,1,1,1,0,0,1),  # 3
    (0,1,1,0,0,1,1),  # 4
    (1,0,1,1,0,1,1),  # 5
    (1,0,1,1,1,1,1),  # 6
    (1,1,1,0,0,0,0),  # 7
    (1,1,1,1,1,1,1),  # 8
    (1,1,1,1,0,1,1)   # 9
]

GPIO.setmode(GPIO.BCM)
GPIO.setup(switch, GPIO.IN, pull_up_down = GPIO.PUD_UP)

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)


try:
    while True:
    	if GPIO.input(switch) == False:
    		print('push')
    		time.sleep(0.5)
    		current_num = (current_num + 1) % 10
    		for i in range(7):
    			GPIO.output(segments[i], num[current_num][i])
    			
except KeyboardInterrupt:
    GPIO.cleanup()
