import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

#constant speed 343(m/s)
v = 343

#set trigger and echo pin
TRIG = 16
E = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(E, GPIO.IN)
GPIO.output(TRIG, GPIO.LOW)

LED_PIN = 12
GPIO.setup(LED_PIN, GPIO.OUT)

#LED shine in 3 three seconds
def shine():
    for i in range(3):
    	GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.5)    

#LED turn on in three seconds
def turn_on():
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(LED_PIN, GPIO.LOW)


#measure the distance
def measure():
    #create pulse with interval 0.00001 second
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)

    pulse_start = 0
    pulse_end = 0
    while GPIO.input(E) == GPIO.LOW:
        pulse_start = time.time()
    while GPIO.input(E) == GPIO.HIGH:
        pulse_end = time.time()

    #echo travel time
    t = pulse_end - pulse_start
    
    #distance = time * velocity
    d = t * v
    d = d / 2
    return d * 100

try:
    while(1):
        distance = measure()
        print(distance)

        #keep the led off
        if distance > 20:
            pass

        #LED shine
        elif distance <= 20 and distance >= 10:
            shine()
        
        #LED turn on
        else:
            turn_on()
        time.sleep(3)

except KeyboardInterrupt:
    print('stop')

finally:
    GPIO.cleanup()
