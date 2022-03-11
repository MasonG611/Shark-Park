from gpiozero import LED
import RPi.GPIO as GPIO

from time import sleep

red = LED(21)
blue = LED(16)
green = LED(20)


red.on()
sleep(2)
red.off()
sleep(.5)
green.on()
sleep(2)
green.off()
sleep(.5)
blue.on()
sleep(2)
blue.off()
sleep(.5)

GPIO.cleanup()