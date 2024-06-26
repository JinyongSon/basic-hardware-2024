import RPi.GPIO as GPIO
import time

segments = (21, 22, 23, 24, 25, 26, 27)
digits = (13, 6, 5, 16)

num = [
    (1, 1, 1, 1, 1, 1, 0),  # 0
    (0, 1, 1, 0, 0, 0, 0),  # 1
    (1, 1, 0, 1, 1, 0, 1),  # 2
    (1, 1, 1, 1, 0, 0, 1),  # 3
    (0, 1, 1, 0, 0, 1, 1),  # 4
    (1, 0, 1, 1, 0, 1, 1),  # 5
    (1, 0, 1, 1, 1, 1, 1),  # 6
    (1, 1, 1, 0, 0, 0, 0),  # 7
    (1, 1, 1, 1, 1, 1, 1),  # 8
    (1, 1, 1, 1, 0, 1, 1)   # 9
]

GPIO.setmode(GPIO.BCM)

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)

for digit in digits:
    GPIO.setup(digit, GPIO.OUT)

try:
    while True:

except KeyboardInterrupt:
	GPIO.cleanup()
