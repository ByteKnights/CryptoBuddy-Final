# LCD Driver Library
# Based on Marix Orbital Specification
# Author: Wyatt Phillips

ESCAPE = 0xFE

def lcdWrite(data):
    print(data)

def display(enabled): 
    if enabled:
        lcdWrite(ESCAPE)
        lcdWrite(0x42)
    else:
        lcdWrite(ESCAPE)
        lcdWrite(0x46)

def setBrightness(val):
    lcdWrite(ESCAPE)
    lcdWrite(0x99)
    lcdWrite(val)

def saveBrightness(val):
    lcdWrite(ESCAPE)
    lcdWrite(0x98)
    lcdWrite(val)

def setContrast(val):
    lcdWrite(ESCAPE)
    lcdWrite(0x50)
    lcdWrite(val)

def saveContrast(val):
    lcdWrite(ESCAPE)
    lcdWrite(0x91)
    lcdWrite(val)

def autoscroll(enabled):
    if enabled:
        lcdWrite(ESCAPE)
        lcdWrite(0x51)
    else:
        lcdWrite(ESCAPE)
        lcdWrite(0x52)

def clear():
    lcdWrite(ESCAPE)
    lcdWrite(0x58)

def setSplash():
    lcdWrite(ESCAPE)
    lcdWrite(0x40)

def setCursor(x,y):
    lcdWrite(ESCAPE)
    lcdWrite(0x47)
    lcdWrite(x)
    lcdWrite(y)

def cursorHome():
    lcdWrite(ESCAPE)
    lcdWrite(0x48)

def cursorBackward():
    lcdWrite(ESCAPE)
    lcdWrite(0x4C)

def cursorForward():
    lcdWrite(ESCAPE)
    lcdWrite(0x4D)

def underlineCursor(enabled):
    if enabled:
        lcdWrite(ESCAPE)
        lcdWrite(0x4A)
    else:
        lcdWrite(ESCAPE)
        lcdWrite(0x4B)

def blinkCursor(enabled):
    if enabled:
        lcdWrite(ESCAPE)
        lcdWrite(0x53)
    else:
        lcdWrite(ESCAPE)
        lcdWrite(0x54)

def setRGB(r,g,b):
    lcdWrite(ESCAPE)
    lcdWrite(0xD0)
    lcdWrite(r)
    lcdWrite(g)
    lcdWrite(b)

def configSize(w,h)
    lcdWrite(ESCAPE)
    lcdWrite(0xD1)
    lcdWrite(w)
    lcdWrite(h)


