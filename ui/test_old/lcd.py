# LCD Driver Library
# Based on Marix Orbital Specification
# Author: Wyatt Phillips

import serial

ESCAPE = 0xFE

class LCD:
    
    def __init__(self, device):
        self.device_name = device
        self.driver = serial.Serial(self.device_name, 9600)
        if not self.driver.is_open:
            self.driver.open()

    def __del__(self):
        self.driver.close()
        del self.driver

    def lcdWrite(self, data, debug=True):
        if debug:
            print(data)
        self.driver.write(chr(data))

    def println(self, text):
        for i in text:
            self.lcdWrite(ord(i), debug=False)

    def display(self, enabled): 
        if enabled:
            self.lcdWrite(ESCAPE)
            self.lcdWrite(0x42)
        else:
            self.lcdWrite(ESCAPE)
            self.lcdWrite(0x46)

    def setBrightness(self, val):
        self.lcdWrite(ESCAPE)
        self.lcdWrite(0x99)
        self.lcdWrite(val)

    def saveBrightness(self, val):
        self.lcdWrite(ESCAPE)
        self.lcdWrite(0x98)
        self.lcdWrite(val)

    def setContrast(self, val):
        self.lcdWrite(ESCAPE)
        self.lcdWrite(0x50)
        self.lcdWrite(val)

    def saveContrast(self, val):
        self.lcdWrite(ESCAPE)
        self.lcdWrite(0x91)
        self.lcdWrite(val)

    def autoscroll(self, enabled):
        if enabled:
            self.lcdWrite(ESCAPE)
            self.lcdWrite(0x51)
        else:
            self.lcdWrite(ESCAPE)
            self.lcdWrite(0x52)

    def clear(self):
        self.lcdWrite(ESCAPE)
        self.lcdWrite(0x58)

    def setSplash(self): # Fix Dis
        self.lcdWrite(ESCAPE)
        self.lcdWrite(0x40)

    def setCursor(self, x, y):
        self.lcdWrite(ESCAPE)
        self.lcdWrite(0x47)
        self.lcdWrite(x)
        self.lcdWrite(y)

    def cursorHome(self):
        self.lcdWrite(ESCAPE)
        self.lcdWrite(0x48)

    def cursorBackward(self):
        self.lcdWrite(ESCAPE)
        self.lcdWrite(0x4C)

    def cursorForward(self):
        self.lcdWrite(ESCAPE)
        self.lcdWrite(0x4D)

    def underlineCursor(self, enabled):
        if enabled:
            self.lcdWrite(ESCAPE)
            self.lcdWrite(0x4A)
        else:
            self.lcdWrite(ESCAPE)
            self.lcdWrite(0x4B)

    def blinkCursor(self, enabled):
        if enabled:
            self.lcdWrite(ESCAPE)
            self.lcdWrite(0x53)
        else:
            self.lcdWrite(ESCAPE)
            self.lcdWrite(0x54)

    def setRGB(self,r,g,b):
        self.lcdWrite(ESCAPE)
        self.lcdWrite(0xD0)
        self.lcdWrite(r)
        self.lcdWrite(g)
        self.lcdWrite(b)

    def configSize(self,w,h):
        self.lcdWrite(ESCAPE)
        self.lcdWrite(0xD1)
        self.lcdWrite(w)
        self.lcdWrite(h)


