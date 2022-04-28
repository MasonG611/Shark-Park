import RPi.GPIO as GPIO
from time import sleep
from mfrc522 import SimpleMFRC522
import serial
GPIO.setwarnings(False)
reader = SimpleMFRC522()
#ser = serial.Serial('/dev/ttyACM0', 19200, timeout=1)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.OUT, initial = GPIO.LOW) #Red -- Closed
GPIO.setup(33, GPIO.OUT, initial = GPIO.LOW) #Green -- Opened


check = ''
file = open('States.txt', 'r+')
file.seek(0, 2)
eof = file.tell()
file.seek(0, 0)
nextLine = True
while nextLine:
    file.readline()
    print(file.tell())
    if file.tell() == (eof-4) or file.tell() == (eof-5):
        check = file.readline()
        nextLine = False
        print('line is ', check)

check.split('\n')

while(True):
   # ser.reset_input_buffer()
    id, text = reader.read()
    sleep(1.5)
    if(id and check.__contains__('Open')):
        GPIO.output(33, GPIO.LOW)
       # ser.write(b"close\n")
        #sleep(5)
        line = ''
        while(line != 'Closed'):
            #line = ser.readline().decode('utf-8').rstrip()
            #line.split('\n')
#         sleep(6)
            line = 'Closed'
            print(line)
        #reader.write(line)
        GPIO.output(31, GPIO.HIGH)
        check = line
        id = ''
    elif(id and check.__contains__('Closed')):
        GPIO.output(31, GPIO.LOW)
        #ser.write(b"open\n")
        line = ''
        while(line != 'Open'):
            #line = ser.readline().decode('utf-8').rstrip()
            #line.split('\n')
            line = 'Open'
            print(line)
            
        #reader.write(line)
        GPIO.output(33, GPIO.HIGH)
        check = line
        id = ''
GPIO.cleanup()
