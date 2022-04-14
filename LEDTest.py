from gpiozero import LED
import RPi.GPIO as GPIO

from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.OUT, initial = GPIO.LOW) #Red -- Closed
GPIO.setup(33, GPIO.OUT, initial = GPIO.LOW)

GPIO.output(31, GPIO.HIGH)
sleep(2)
GPIO.output(31, GPIO.LOW)
GPIO.output(33, GPIO.HIGH)
sleep(2)
GPIO.output(33, GPIO.LOW)

#red.on()
#sleep(2)
#red.off()
# sleep(.5)
# green.on()
# sleep(2)
# green.off()
# sleep(.5)
# blue.on()
# sleep(2)
# blue.off()
# sleep(.5)

GPIO.cleanup()