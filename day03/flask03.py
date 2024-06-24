# URL접속을 /led/on, /led/off 로 접속하면 led를 on,off 하는 웹페이지를 만들자
from flask import Flask
import RPi.GPIO as GPIO

led1 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def led():
	return "Hello led!!"

@app.route("/led/on")
def ledon():
	GPIO.output(led1, False)
	return "led on!!"

@app.route("/led/off")
def ledoff():
	GPIO.output(led1, True)
	return "led off!!"

if __name__ == "__main__":
	try:
		while True:
			app.run(host = "0.0.0.0", port = 10011, debug = True)

	except KeyboardInterrupt:
		GPIO.cleanup()
