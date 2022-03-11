from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT, initial = GPIO.LOW) #Counterclockwise
GPIO.setup(13, GPIO.OUT, initial = GPIO.LOW) #Clockwise

GPIO.output(13, GPIO.HIGH) #clockwise
sleep(3)
GPIO.output(13, GPIO.LOW)
sleep(3)
GPIO.output(15, GPIO.HIGH) #counterclockwise
sleep(3)
GPIO.output(15, GPIO.LOW)


GPIO.cleanup()
