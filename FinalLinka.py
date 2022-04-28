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
    if file.tell() == (eof-1):
        check = file.readline()
        nextLine = False
        print('line is ', check)

check.split('\n')

while(True):
   # ser.reset_input_buffer()
    sleep(.3)
    id = reader.read()
    id = id.strip(' ')
    if(id and not id.isspace()):
        GPIO.output(33, GPIO.LOW)
       # ser.write(b"close\n")
        #sleep(5)
        line = ''
        while(line == ''):
            #line = ser.readline().decode('utf-8').rstrip()
#         sleep(6)
            print(line)
        #reader.write(line)
        GPIO.output(31, GPIO.HIGH)
    elif(check == 'Close'):
        GPIO.output(31, GPIO.LOW)
        #ser.write(b"open\n")
        line = ''
        while(line == ''):
            #line = ser.readline().decode('utf-8').rstrip()
            print(line)
        #reader.write(line)
        GPIO.output(33, GPIO.HIGH)
GPIO.cleanup()
