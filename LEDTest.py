from gpiozero import LED

from time import sleep

red = LED(19)
blue = LED(13)
green = LED(26)

while(True):
    red.on()
    sleep(2)
    red.off()
    sleep(.5)
    blue.on()
    sleep(2)
    blue.off()
    sleep(.5)
    green.on()
    sleep(2)
    green.off()
    sleep(.5)
