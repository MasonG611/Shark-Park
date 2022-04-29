import RPi.GPIO as GPIO
from time import sleep
from mfrc522 import SimpleMFRC522

GPIO.setwarnings(False)

reader = SimpleMFRC522()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.OUT, initial = GPIO.LOW) #Counterclockwise -- Close
GPIO.setup(13, GPIO.OUT, initial = GPIO.LOW) #Clockwise -- Open
GPIO.setup(31, GPIO.OUT, initial = GPIO.LOW) #Red -- Closed
GPIO.setup(33, GPIO.OUT, initial = GPIO.LOW) #Green -- Opened

def Open():
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(31, GPIO.LOW)
    print('opening')
    sleep(5)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(33, GPIO.HIGH)
    print('Open')

def Close():
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(33, GPIO.LOW)
    print('closing')
    sleep(5)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(31, GPIO.HIGH)
    print('Closed')

check = ''
file = open('States.txt', 'r+')
file.seek(0, 2)
eof = file.tell()
file.seek(0, 0)
nextLine = True
while nextLine:
    file.readline()
    print(file.tell())
    if file.tell() == (eof-5) or file.tell() == (eof-7):
        check = file.readline()
        nextLine = False
        print('Last line is: ', check)

check.split('\n')

while(True):
    id, text = reader.read()
    sleep(1.5)
    if(id and check.__contains__('Open')):
        Close()
        file.write('Closed\n')
        check = 'Closed'
        id = ''
    if(id and check.__contains__('Closed')):
        Open()
        file.write('Open\n')
        check = 'Open'
        id = '' 

GPIO.cleanup()