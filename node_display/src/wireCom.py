import RPi.GPIO as GPIO
import time

import src.globals as g


def initOneWire():
    # Setup Pin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.OUT)


def oneWireThread():
    wireTimer:float = 0
    wireTimerMax:float = 0.2

    while not g.killOneWire:
        if wireTimer <= 0:
            writeOneWire(g.railDelay*2)
            print(f"ONE WIRE: {g.railDelay*2}")
            wireTimer = wireTimerMax
        else:
            wireTimer -= (time.time() - g.lastLoopTime)
        g.lastLoopTime = time.time()
        


def writeOneWire(delay):
    GPIO.output(26, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(26, GPIO.LOW)