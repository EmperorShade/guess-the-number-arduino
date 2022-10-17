from cmath import pi
import time
from unicodedata import name
from pyfirmata import SERVO, Arduino, util

pin = 1
port = ''
board = Arduino(port)

board.digital[11].mode = SERVO

def rotateservo(pin, angle):
    board.digital[pin].write(angle)
    time.sleep(0.015)

while True:
    for i in range(0, 180):
        rotateservo(pin, i)
    for i in range(180, 1, -1):
        rotateservo(pin, i)