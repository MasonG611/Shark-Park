import RPi.GPIO as GPIO
from time import sleep
from mfrc522 import SimpleMFRC522
import serial

reader = SimpleMFRC522()
ser = serial.Serial('/dev/ttyACM0', 19200, timeout=1)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.OUT, initial = GPIO.LOW) #Red -- Closed
GPIO.setup(33, GPIO.OUT, initial = GPIO.LOW) #Green -- Opened
GPIO.setwarnings(False)

again = 'Y'

while(again == 'Y'):
    ser.reset_input_buffer()
    sleep(.3)
    id, check = reader.read()
    check = check.strip(' ')
    if(check == 'opened'):
        GPIO.output(33, GPIO.LOW)
        ser.write(b"close\n")
        #sleep(5)
        line = ''
        while(line == ''):
            line = ser.readline().decode('utf-8').rstrip()
#         sleep(6)
        print(line)
        reader.write(line)
        GPIO.output(31, GPIO.HIGH)
        again = input('Would you like another iteration? Y/N: ')
    elif(check == 'closed'):
        GPIO.output(31, GPIO.LOW)
        ser.write(b"open\n")
        line = ''
        while(line == ''):
            line = ser.readline().decode('utf-8').rstrip()
        print(line)
        reader.write(line)
        GPIO.output(33, GPIO.HIGH)
        again = input('Would you like another iteration? Y/N: ')
GPIO.cleanup()
