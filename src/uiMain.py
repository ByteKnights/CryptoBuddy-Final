import driver
import math
import serialSend
import pgp
import findPort
import lifesaver
import subprocess

device_name = "/dev/ttyACM0"

width = 20
height = 4
text = []
curPos = 1

screen = driver.Driver(device_name, width, height)
screen.configSize(width, height)
screen.blinkCursor(True)
screen.clear()

def whipe():
    text = []
    curPos = 1;
    screen.clear()

def update():
    screen.clear()
    screen.println(text)
    screen.setCursor(curPos % 20, math.trunc(curPos))

while True:
    key = lifesaver.getch()
    if key == '\x1b':
        # serialSend.send("/dev/ttyACM1", str(pgp.encrypt(''.join(text))))
        print(''.join(text))
        cypherText = pgp.encrypt(''.join(text))
        subprocess.call("echo '" + cypherText[0:100] + "' >> /dev/ttyACM1", shell=True)
        subprocess.call("echo '" + cypherText[100:200] + "' >> /dev/ttyACM1", shell=True)
        subprocess.call("echo '" + cypherText[300:300] + "' >> /dev/ttyACM1", shell=True)
        subprocess.call("echo '" + cypherText[400:400] + "' >> /dev/ttyACM1", shell=True)
        subprocess.call("echo '" + cypherText[500:500] + "' >> /dev/ttyACM1", shell=True)
        subprocess.call("echo '" + cypherText[600:600] + "' >> /dev/ttyACM1", shell=True)
        subprocess.call("echo '" + cypherText[700:700] + "' >> /dev/ttyACM1", shell=True)
        subprocess.call("echo '" + cypherText[800:800] + "' >> /dev/ttyACM1", shell=True)
        subprocess.call("echo '" + cypherText[900:] + "' >> /dev/ttyACM1", shell=True)
        text = []


    '''
    if key == Key.space:
        text.append(' ')
        curPos = 1
        update()
    elif key == Key.backspace:
        if len(text) > 0:
            del text[len(text)-1]
            curPos = 1
            update()
    elif key == Key.shift or key == Key.ctrl:
        print(key)
    if key == Key.esc:
        print(type(text))
    '''
    text.append(key)
    curPos = 1
    update()
