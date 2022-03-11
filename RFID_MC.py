import RPi.GPIO as GPIO
from time import sleep
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT, initial = GPIO.LOW) #Counterclockwise -- Open
GPIO.setup(13, GPIO.OUT, initial = GPIO.LOW) #Clockwise -- Close

check = ''

again = 'Y'

while(check == ''):
    id, check = reader.read()

while(again == 'Y'):
    sleep(.3)
    check = check.strip(' ')
    if(check == 'Open'):
        GPIO.output(13, GPIO.HIGH)
        print('closing')
        sleep(5)
        GPIO.output(13, GPIO.LOW)
        reader.write('Closed')
        print('Closed')
        id, check = reader.read()
        again = input('Would you like another iteration? Y/N: ')
    elif(check == 'Closed'):
        GPIO.output(15, GPIO.HIGH)
        print('opening')
        sleep(5)
        GPIO.output(15, GPIO.LOW)
        reader.write('Open')
        print('Open')
        id, check = reader.read()
        again = input('Would you like another iteration? Y/N: ')
GPIO.cleanup()
