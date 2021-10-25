from time import sleep
import RPi.GPIO as GPIO

DIR = 20  # Direction GPIO Pin
STEP = 21 # Step GPIO Pin
CW = 1    # Clockwise Rotation
CCW = 0   # Counterclockwise Rotation
SPR = 48  # Steps per Revolution (360/7.5)

MODE = (14, 15, 18)
GPIO.setup(MODE, GPIO.OUT)
RESOLUTION = {'Full' : (0, 0, 0),
	      'Half' : (1, 0, 0),
	      '1/4'  : (0, 1, 0),
	      '1/8'  : (1, 1, 0),
	      '1/16' : (0, 0, 1),
	      '1/32' : (1, 0, 1)}
GPIO.output(MODE, RESOLUTION['Full'])

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(DIR, CW)

step_count = SPR
delay = .0208

for x in range(step_count):
	GPIO.output(STEP, GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEP, GPIO.LOW)
	sleep(delay)

slee(.5)
GPIO.output(DIR, CCW)
	GPIO.output(STEP, GPIO.HIGH)
	sleep(delay)
	GPIO.output(STEP, GPIO.LOW)
	sleep(delay)
