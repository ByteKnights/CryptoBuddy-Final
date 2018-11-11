from src import serialSend
from src import pgp
from src import findPort

cipher = pgp.encrypt("hello World", "testUser1")
serialSend.send(findPort.findScreen(), cipher)

