import RPi.GPIO as GPIO
from time import sleep
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

GPIO.setup(36, GPIO.OUT, initial = GPIO.LOW) #blue
GPIO.setup(38, GPIO.OUT, initial = GPIO.LOW) #green
GPIO.setup(40, GPIO.OUT, initial = GPIO.LOW) #red

check = ''

while(check == ''):
    id, check = reader.read()

while(True):
    sleep(.3)
    if(check == 'Open'):
        GPIO.output(38, GPIO.LOW)
        GPIO.output(36, GPIO.HIGH)
        print('closing')
        sleep(3)
        GPIO.output(36, GPIO.LOW)
        GPIO.output(40, GPIO.HIGH)
        reader.write('Closed')
        print('Closed')
        id, check = reader.read()
    elif(check == 'Closed'):
        GPIO.output(40, GPIO.LOW)
        GPIO.output(36, GPIO.HIGH)
        print('opening')
        sleep(3)
        GPIO.output(36, GPIO.LOW)
        GPIO.output(38, GPIO.HIGH)
        reader.write('Open')
        print('Open')
        id, check = reader.read()
GPIO.cleanup()