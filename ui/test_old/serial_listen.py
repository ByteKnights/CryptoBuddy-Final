import serial
import sys
import time

TIMEOUT = 1000 # The amount of time to wait for input before closing

def getTime():
    return int(round(time.time() * 1000))

arduino = serial.Serial('/dev/ttyUSB0',9600)
print('UART Serial connection made @ ' + arduino.name + '\n')

while (arduino.in_waiting <= 0):
    pass

timelog = getTime()
while (getTime()-timelog < TIMEOUT):
    if (arduino.in_waiting > 0):
        sys.stdout.write(arduino.read(1))
        timelog = getTime()

arduino.close()
