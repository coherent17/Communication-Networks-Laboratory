import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

v = 343
TRIG = 16
E = 18

print('1')
GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(E, GPIO.IN)
GPIO.output(TRIG, GPIO.LOW)

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

while(1):
    print(measure())
    time.sleep(1)

GPIO.cleanup()
