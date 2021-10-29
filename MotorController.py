from time import sleep
import RPi.GPIO as GPIO

DIR = 20   # Direction GPIO Pin
STEP = 21  # Step GPIO Pin
CW = 0     # Clockwise Rotation
CCW = 1    # Counterclockwise Rotation
SPR = 48   # Steps per Revolution (360 / 7.5)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)

step_count = SPR
delay = .0208

check = int(input("press 1 for clockwise 2 for counterclockwise: "))

while(1):
	if check == 1:
		GPIO.output(DIR, CW)
		for x in range(step_count):
			GPIO.output(STEP, GPIO.HIGH)
			sleep(delay)
			GPIO.output(STEP, GPIO.LOW)
			sleep(delay)
		check = int(input('press 1 for clockwise 2 for counterclockwise: '))
	
	elif check == 2:
		GPIO.output(DIR, CCW)
		for x in range(step_count):
			GPIO.output(STEP, GPIO.HIGH)
			sleep(delay)
			GPIO.output(STEP, GPIO.LOW)
			sleep(delay)
		check = int(input('press 1 for clockwise 2 for counterclockwise: '))
	else:
		check = int(input('Error: incorrect input. 1 for CW 2 for CCW: '))
		
	

GPIO.cleanup()
