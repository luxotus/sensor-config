import sys, os
import time
import RPi.GPIO as GPIO
import sqlite3
sys.path.insert(0, os.path.abspath('..'))
from Libraries.usefulFunctions import *
from datetime import datetime
import calendar

d = datetime.utcnow()
unixtime = calendar.timegm(d.utctimetuple())

GPIO.setmode(GPIO.BCM)

# SPI port on the ADC to the Cobbler
SPICLK = 18
SPIMISO = 23
SPIMOSI = 24
SPICS = 25

# set up the SPI interface pins
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPICS, GPIO.OUT)

# PH sensor connected to analog pin 0 on the MCP3008
phAnalogSensor = 0

if __name__ == '__main__':
    try:
        while True:
            phAnalogValue = readAnalogDigitalConverter(phAnalogSensor, SPICLK, SPIMOSI, SPIMISO, SPICS)
            # print "PH Analog Value: ", phAnalogValue
            # print "Temp: " + str(read_temp()) + "F"
            print "(" + str(read_temp()) + "," + str(phAnalogValue) + "," + str(unixtime) + ")"
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()