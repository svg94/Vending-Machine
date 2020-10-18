#!/usr/bin/env python3
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

A = [7, 19,8,18]			#Each Stepper Motor has 4 Wireslots  
B = [11,21,10,22]			# represented by the lists A,B,C,D
C = [13, 23,12,24]		# Slot 1 is A, Slot 2 is B... 
D = [15, 29,16,26]		#4 Motors, so 4 elements in each list. (soon)
pins= [A,B,C,D]

for pinblock in pins:		#Setup all the pins
	for pin in pinblock:
		GPIO.setup(pin, GPIO.OUT)

def GPIO_SETUP(a,b,c,d,motor):	#which Motor 0-3
    GPIO.output(A[motor],a)
    GPIO.output(B[motor],b)
    GPIO.output(C[motor],c)
    GPIO.output(D[motor],d)
    time.sleep(0.002)

for i in range(len(A)):#Taking A, assuming every list has equal length
		GPIO_SETUP(0,0,0,0,i)
	

for i in range(500):
    GPIO_SETUP(1,1,0,0,0)
    GPIO_SETUP(0,1,1,0,0)
    GPIO_SETUP(0,0,1,1,0)
    GPIO_SETUP(1,0,0,1,0)

for i in range(500):
    GPIO_SETUP(1,1,0,0,1)
    GPIO_SETUP(0,1,1,0,1)
    GPIO_SETUP(0,0,1,1,1)
    GPIO_SETUP(1,0,0,1,1)

for i in range(500):
    GPIO_SETUP(1,1,0,0,2)
    GPIO_SETUP(0,1,1,0,2)
    GPIO_SETUP(0,0,1,1,2)
    GPIO_SETUP(1,0,0,1,2)

for i in range(500):
    GPIO_SETUP(1,1,0,0,3)
    GPIO_SETUP(0,1,1,0,3)
    GPIO_SETUP(0,0,1,1,3)
    GPIO_SETUP(1,0,0,1,3)




#for i in range(2000):      #Wave Rotation. Very Basic not so precise or fast.
#   GPIO_SETUP(1,0,0,0)
#  GPIO_SETUP(0,1,0,0)
# GPIO_SETUP(0,0,1,0)
# GPIO_SETUP(0,0,0,1)
for i in range(len(A)):
	GPIO_SETUP(0,0,0,0,i)

