import sys, os
import time
import RPi.GPIO as GPIO
sys.path.insert(0, os.path.abspath('..'))
print(os.path.abspath('..'))
from Libraries.usefulFunctions import readAnalogDigitalConverter

GPIO.setmode(GPIO.BCM)
DEBUG = 1

# change these as desired - they're the pins connected from the
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

# Analog pins starting with 0
analogSensor_01 = 0; 

if __name__ == '__main__':
    try:
        while True:
            # read the analog pin
            analogValue_01 = readAnalogDigitalConverter(analogSensor_01, SPICLK, SPIMOSI, SPIMISO, SPICS)
            
            print "analog value: ", analogValue_01 
            time.sleep(1)
    # Stop on Ctrl+C and clean up
    except KeyboardInterrupt:
        GPIO.cleanup()