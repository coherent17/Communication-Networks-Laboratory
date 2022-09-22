#!/usr/bin/python
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
LED_PIN = 12
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)


# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('Usage: sudo ./Adafruit_DHT.py [11|22|2302] <GPIO pin number>')
    print('Example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO pin #4')
    sys.exit(1)

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}  Humidity={1:0.1f}%'.format(temperature, humidity))
    temperature_threshold = 25
    if temperature > temperature_threshold:
        print('Temperature is over %d degree' %(temperature_threshold))
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(10)                  #turn on LED for 10 seconds
    GPIO.cleanup()

else:
    print('Failed to get reading. Try again!')
    sys.exit(1)
