from gpiozero import LED

from time import sleep

red = LED(21)
blue = LED(16)
green = LED(20)

while(True):
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
