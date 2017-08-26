import dht11
import RPi.GPIO as GPIO
import time

# 3v, GPIO 14

Temp_sensor = 14
instance = dht11.DHT11(Temp_sensor)
GPIO.setmode(GPIO.BCM)

while True:
    result = instance.read()

    if result.is_valid():
        print 'temp: '+str(result.temperature)
        print 'humid: '+str(result.humidity)
	time.sleep(2)

GPIO.cleanup()
