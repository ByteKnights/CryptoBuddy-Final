import lcd
import time

def splashAbout(screen):
    screen.setRGB(0,255,0)
    screen.setContrast(200)
    screen.setBrightness(100)
    screen.clear()
    screen.cursorHome()

    screen.setCursor(1,2)
    screen.println("  CryptoBuddy 1.0")
    screen.setCursor(1,3)
    screen.println("  By Byte Knights")

def splashTitle(screen):
    screen.setRGB(255,0,0)
    screen.setContrast(255)
    screen.setBrightness(200)
    screen.clear()
    screen.cursorHome()

    screen.println("Byte Knights:")
    screen.setCursor(1,2)
    screen.println("CryptoBuddy TM")

screenTop = lcd.LCD('/dev/ttyACM0')
screenBottom = lcd.LCD('/dev/ttyACM1')

print("UART Serial established @ " + screenTop.driver.name)
print("UART Serial established @ " + screenBottom.driver.name)

screenTop.configSize(20,4)
screenBottom.configSize(20,4)

splashAbout(screenTop)

screenBottom.setRGB(0,0,255)
screenBottom.setContrast(255)
screenBottom.setBrightness(200)
screenBottom.clear()
screenBottom.cursorHome()
