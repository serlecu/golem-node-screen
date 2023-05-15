import RPi.GPIO as GPIO
import time
import serial
import serial.tools.list_ports

import src.globals as g


# ========= RAIL SERIAL =========

def findSerial():
    ports = serial.tools.list_ports.comports()
    for port in ports:
        print(f"{port.device} :::: {port.name}")
    time.sleep(100)
    

def openSerial(s, port:str):
    arduino = serial.Serial(port, 9600)
    
    


def sendValueSerial(value: int):
    
    arduino.write(b'9')



# ========= ONE WIRE =========
def initOneWire():
    # Setup Pin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.OUT)


def oneWireThread():
    wireTimer:float = 0
    wireTimerMax:float = 1

    while not g.killOneWire:
        GPIO.output(26, GPIO.HIGH)
        time.sleep(g.railDelay*4000) # railDelay is [0./1.]
        GPIO.output(26, GPIO.LOW)

        print(f"ONE WIRE: {g.railDelay*2}")
        time.sleep(1000)
        


def writeOneWire(delay):
    GPIO.output(26, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(26, GPIO.LOW)