import RPi.GPIO as GPIO
import time
import socket
import sys, select

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

#connect TCP socket to server
HOST = '172.20.10.7'
PORT = 8001

#IPV4, TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))



#LED shine in 3 three seconds
def shine():
    for i in range(5):
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

        i, o, e = select.select([sys.stdin], [], [], 3)
        if(i):
            a = sys.stdin.readline().strip()
            client.sendall(a)
        else:
            print('Nothing')
            

        if distance < 10:
            client.sendall('s')

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
