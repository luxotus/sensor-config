import sys, os
import time
import RPi.GPIO as GPIO
sys.path.insert(0, os.path.abspath('..'))
print(os.path.abspath('..'))
# from Libraries.usefulFunctions import *

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
phAnalogValue = 0; 

def readAnalogDigitalConverter(adcnum, clockpin, mosipin, misopin, cspin):
    if ((adcnum > 7) or (adcnum < 0)):
        return -1
    GPIO.output(cspin, True)

    GPIO.output(clockpin, False)  # start clock low
    GPIO.output(cspin, False)     # bring CS low

    commandout = adcnum
    commandout |= 0x18  # start bit + single-ended bit
    commandout <<= 3    # we only need to send 5 bits here
    for i in range(5):
        if (commandout & 0x80):
            GPIO.output(mosipin, True)
        else:
            GPIO.output(mosipin, False)
        commandout <<= 1
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)

    adcout = 0
    # read in one empty bit, one null bit and 10 ADC bits
    for i in range(12):
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)
        adcout <<= 1
        if (GPIO.input(misopin)):
            adcout |= 0x1

    GPIO.output(cspin, True)
        
    adcout >>= 1       # first bit is 'null' so drop it
    return adcout

if __name__ == '__main__':
    try:
        while True:
            # read the analog pin
            phAnalogValue = readAnalogDigitalConverter(phAnalogValue, SPICLK, SPIMOSI, SPIMISO, SPICS)
            
            print "PH Analog Value: " + str(phAnalogValue)
            #print "Temp: " + str(read_temp()) + "F"
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()