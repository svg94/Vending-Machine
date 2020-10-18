import time
import RPi.GPIO as GPIO
#Class for Motors
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

class Motor:
	def __init__(self,pA,pB,pC,pD):
  	self.A = pA
		GPIO.setup(self.A, GPIO.OUT)
		self.B = pB
		GPIO.setup(self.A, GPIO.OUT)
		self.C = pC
		GPIO.setup(self.A, GPIO.OUT)
		self.D = pD
		GPIO.setup(self.A, GPIO.OUT)
		GPIO_SETUP(0,0,0,0)
	def GPIO_SETUP(self,a,b,c,d):
		GPIO.output(self.A,a)
		GPIO.output(self.B,b)
		GPIO.output(self.C,c)
		GPIO.output(self.D,d)
		time.sleep(0.002)
	def Turn_Right(self,x):      #x: How much should the motor spin
		GPIO_SETUP(0,0,0,0)
		for i in range((x * 2)):  #* 2 because one cicle of the motor consist of 8 steps
			GPIO_SETUP(1,1,0,0)
			GPIO_SETUP(0,1,1,0)
			GPIO_SETUP(0,0,1,1)
			GPIO_SETUP(1,0,0,1)
		GPIO_SETUP(0,0,0,0)
	def Turn_Left(self,x):
		GPIO_SETUP(0,0,0,0)
		for i in range((x * 2)):  #* 2 because one cicle of the motor consist of 8 steps
			GPIO_SETUP(1,0,0,1)  #For turning left just do turn right backwards.
			GPIO_SETUP(0,0,1,1)
			GPIO_SETUP(0,1,1,0)
			GPIO_SETUP(1,1,0,0)
		GPIO_SETUP(0,0,0,0)
