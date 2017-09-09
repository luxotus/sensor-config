import sys, os
import time
import RPi.GPIO as GPIO
sys.path.insert(0, os.path.abspath('..'))
from Libraries.usefulFunctions import *

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

if __name__ == '__main__':
    try:
        while True:
            # PH sensor connected to analog pin 0 on the MCP3008
            phAnalogValue = 0
            phAnalogValue = readAnalogDigitalConverter(phAnalogValue, SPICLK, SPIMOSI, SPIMISO, SPICS)
            
            print "PH Analog Value: ", phAnalogValue
            print "Temp: " + str(read_temp()) + "F"
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()