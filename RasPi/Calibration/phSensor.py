import sys, os
import time
import glob
import RPi.GPIO as GPIO
sys.path.insert(0, os.path.abspath('..'))
print(os.path.abspath('..'))
from Libraries.usefulFunctions import *

GPIO.setmode(GPIO.BCM)
DEBUG = 1

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

# DS18B20 temperature sensor
# gpio 7, 3.3v, connect vcc to data pin with 4.7k ohms 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

if __name__ == '__main__':
    try:
        while True:
            # read the analog pin
            phAnalogValue = readAnalogDigitalConverter(phAnalogValue, SPICLK, SPIMOSI, SPIMISO, SPICS)
            
            print "PH Analog Value: " + str(phAnalogValue)
            print "Temp: " + str(read_temp()) + "F"
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()