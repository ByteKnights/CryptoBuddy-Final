import serial


def send(port, data):
    s = serial.Serial(port)
    s.write(data)
