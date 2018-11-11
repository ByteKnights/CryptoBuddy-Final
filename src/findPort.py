import subprocess

def findParticle():
    if str(subprocess.call("udevadm info /dev/ttyACM0 | head -3 | tail -1", shell=True)) == "S: serial/by-id/usb-Particle_Photon_2c0027001051363036373538-if00":
        print("Particle @/dev/ttyACM0")
        return "/dev/ttyACM0"
    else:
        print("Particle @/dev/ttyACM1")
        return "/dev/ttyACM1"
def findScreen():
    if str(subprocess.call("udevadm info /dev/ttyACM0 | head -3 | tail -1", shell=True)) == "S: serial/by-id/usb-239a_Adafruit_Industries-if00":
        print("Screen @/dev/ttyACM0")
        return "/dev/ttyACM0"
    else:
        print("Screen @/dev/ttyACM1")
        return "/dev/ttyACM1"
