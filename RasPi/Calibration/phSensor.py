import sys, os
import time
import RPi.GPIO as GPIO
import sqlite3
sys.path.insert(0, os.path.abspath('..'))
from Libraries.usefulFunctions import *
from datetime import datetime
import calendar

conn = sqlite3.connect('phCal.db')
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS phCal(sampleName TEXT, temperature INTEGER, analog INTEGER, currentDateTime DATETIME)")
conn.commit()

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

# Name of sample
sampleName = "Air"

# PH sensor connected to analog pin 0 on the MCP3008
phAnalogSensor = 0

if __name__ == '__main__':
    try:
        while True:
            unixtime = calendar.timegm(datetime.utcnow().utctimetuple())
            # print( datetime.fromtimestamp(int(unixtime)).strftime('%Y-%m-%d %H:%M:%S'))
            
            phAnalogValue = readAnalogDigitalConverter(phAnalogSensor, SPICLK, SPIMOSI, SPIMISO, SPICS)
            print "(" + str(read_temp()) + "," + str(phAnalogValue) + "," + str(unixtime) + ")"
            c.execute("INSERT INTO phCal VALUES (?,?,?,?)", (sampleName, read_temp(), phAnalogValue, unixtime))
            conn.commit()
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()