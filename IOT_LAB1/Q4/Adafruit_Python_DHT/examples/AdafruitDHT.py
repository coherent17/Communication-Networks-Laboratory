#!/usr/bin/python
import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

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

v = 331 + 0.6 * temperature
print('Temp = %d' %(temperature))
print('%d = 331 + 0.6 * %d' %(v, temperature))
TRIG = 16
E = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(E, GPIO.IN)
GPIO.output(TRIG, GPIO.LOW)
LED_PIN = 12
GPIO.setup(LED_PIN,GPIO.OUT)
GPIO.output(LED_PIN,GPIO.LOW)

def measure():
    
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)
    pulse_start = 0
    pulse_end = 0
    while GPIO.input(E) == GPIO.LOW:
        pulse_start = time.time()
    while GPIO.input(E) == GPIO.HIGH:
        pulse_end = time.time()

    t = pulse_end - pulse_start
    d = t * v
    d = d / 2
    return d * 100


def shine():
    for i in range(3):
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.5)


def turn_on():
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(LED_PIN, GPIO.LOW)


try:
    while(1):
        distance = measure()
        print(distance)
        if distance > 20:
            pass
        elif distance <= 20 and distance >= 10:
            shine()
        else:
            turn_on()
        time.sleep(3)

except KeyboardInterrupt:
    print('stop')

finally:
    GPIO.cleanup()