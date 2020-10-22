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
		GPIO.setup(self.B,GPIO.OUT)
		self.C = pC
		GPIO.setup(self.C,GPIO.OUT)
		self.D = pD
		GPIO.setup(self.D,GPIO.OUT)

	def GPIO_SETUP(self, a, b, c, d):
		GPIO.output(self.A,a)
		GPIO.output(self.B,b)
		GPIO.output(self.C,c)
		GPIO.output(self.D,d)
		time.sleep(0.002)

	def Turn_Right(self, x): #x: How much to spin right
		self.GPIO_SETUP(0,0,0,0)
		y = x*2	#times 2 because one motor cicle is 8 steps
		for i in range(y):
			self.GPIO_SETUP(1,1,0,0)
			self.GPIO_SETUP(0,1,1,0)
			self.GPIO_SETUP(0,0,1,1)
			self.GPIO_SETUP(1,0,0,1)
		self.GPIO_SETUP(0,0,0,0)
	def Turn_Left(self,x):
		self.GPIO_SETUP(0,0,0,0)
		y=x*2
		for i in range(y):			
			self.GPIO_SETUP(1,0,0,1)
			self.GPIO_SETUP(0,0,1,1)
			self.GPIO_SETUP(0,1,1,0)
			self.GPIO_SETUP(1,1,0,0)
		self.GPIO_SETUP(0,0,0,0)
