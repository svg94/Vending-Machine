import time
import RPi.GPIO as GPIO
from flask import Flask, request, render_template

app = Flask(__name__)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
A = 7   #TO-DO: Put PinNumbers in list
B = 11
C = 13
D = 15

GPIO.setup(A, GPIO.OUT)
GPIO.setup(B,GPIO.OUT)
GPIO.setup(C,GPIO.OUT)
GPIO.setup(D,GPIO.OUT)

def GPIO_SETUP(a,b,c,d):
	GPIO.output(A,a)
	GPIO.output(B,b)
	GPIO.output(C,c)
	GPIO.output(D,d)
	time.sleep(0.002)

@app.route('/', methods=['GET'])
def index():
	status = request.args.get('status')	
	text=""
	if status == 'succ':				
		GPIO_SETUP(0,0,0,0)
		for i in range(500):
			for i in range(2):		#One Motor cicle is 8 steps.    
				GPIO_SETUP(1,1,0,0)
				GPIO_SETUP(0,1,1,0)
				GPIO_SETUP(0,0,1,1)
				GPIO_SETUP(1,0,0,1)
		text="Snack retrieved. Don't get any more, bro. It's for your own health."
		return render_template("index.html",name=text
	GPIO_SETUP(0,0,0,0)
	return render_template("index.html",name =text)	

if __name__ == "__main__":
	app.run()
