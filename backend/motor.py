import time
import RPi.GPIO as GPIO
#MY CLASS FOR THE MOTORS
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

class Motor:
	def __init__(self, pA, pB, pC, pD):
		self.A = pA
		GPIO.setup(self.A,GPIO.OUT)
		self.B = pB
		GPIO.setup(self.A,GPIO.OUT)
		self.C = pC
		GPIO.setup(self.A,GPIO.OUT)
		self.D = pD
		GPIO.setup(self.A,GPIO.OUT)
		GPIO_SETUP(0,0,0,0)
	def GPIO_SETUP(self,a,b,c,d):
		GPIO.output(self.A,a)
		GPIO.output(self.B,b)
		GPIO.output(self.C,c)
		GPIO.output(self.D,d)
		time.sleep(0.002)
	def Turn_Right(self, x): #x: How much to spin right
		GPIO_SETUP(0,0,0,0)
		y = x*2	#times 2 because one motor cicle is 8 steps
		for i in range(y):
			GPIO_SETUP(1,1,0,0)
			GPIO_SETUP(0,1,1,0)
			GPIO_SETUP(0,0,1,1)
			GPIO_SETUP(1,0,0,1)
		GPIO_SETUP(0,0,0,0)
	def Turn_Left(self,x):
		GPIO_SETUP(0,0,0,0)
		y=x*2
		for i in range(y):			
			GPIO_SETUP(1,0,0,1)
			GPIO_SETUP(0,0,1,1)
			GPIO_SETUP(0,1,1,0)
			GPIO_SETUP(1,1,0,0)
		GPIO_SETUP(0,0,0,0)
