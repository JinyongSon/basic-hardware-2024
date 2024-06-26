import RPi.GPIO as GPIO
import time

segments = (21, 22, 23, 24, 25, 26, 27)

digits = (13, 6, 5, 16)

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
for segment in segments:
    GPIO.setup(segment, GPIO.OUT)

for digit in digits:
	GPIO.setup(digit, GPIO.OUT)

try:
    while True:
        GPIO.output(segments[0], num[1][0])
        GPIO.output(segments[1], num[2][1])
        GPIO.output(segments[2], num[3][2])
        GPIO.output(segments[3], num[4][3])

        GPIO.output(digits[0], GPIO.HIGH)
        time.sleep(1)
        GPIO.output(digits[0], GPIO.LOW)

        GPIO.output(digits[1], GPIO.HIGH)
        time.sleep(1)
        GPIO.output(digits[1], GPIO.LOW)

        GPIO.output(digits[2], GPIO.HIGH)
        time.sleep(1)
        GPIO.output(digits[2], GPIO.LOW)

        GPIO.output(digits[3], GPIO.HIGH)
        time.sleep(1)
        GPIO.output(digits[3], GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()
