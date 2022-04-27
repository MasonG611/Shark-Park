import RPi.GPIO as GPIO
from time import sleep
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT, initial = GPIO.LOW) #Counterclockwise -- Close
GPIO.setup(13, GPIO.OUT, initial = GPIO.LOW) #Clockwise -- Open
GPIO.setup(31, GPIO.OUT, initial = GPIO.LOW) #Red -- Closed
GPIO.setup(33, GPIO.OUT, initial = GPIO.LOW) #Green -- Opened

again = 'Y'

while(again == 'Y'):
    sleep(.3)
    id, check = reader.read()
    check = check.strip(' ')
    if(check == 'Open'):
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(33, GPIO.LOW)
        print('closing')
        sleep(5)
        GPIO.output(15, GPIO.LOW)
        reader.write('Closed')
        GPIO.output(31, GPIO.HIGH)
        print('Closed')
        again = input('Would you like another iteration? Y/N: ')
    elif(check == 'Closed'):
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(31, GPIO.LOW)
        print('opening')
        sleep(5)
        GPIO.output(13, GPIO.LOW)
        reader.write('Open')
        GPIO.output(33, GPIO.HIGH)
        print('Open')
        again = input('Would you like another iteration? Y/N: ')
GPIO.cleanup()
