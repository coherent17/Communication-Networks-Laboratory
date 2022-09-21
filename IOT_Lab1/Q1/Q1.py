import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
LED_PIN = 12
GPIO.setup(LED_PIN, GPIO.OUT)
unit = 0.3


def dot():
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(1 * unit)
    GPIO.output(LED_PIN, GPIO.LOW)

def dash():
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(3 * unit)
    GPIO.output(LED_PIN, GPIO.LOW)

def space_between_same_letter():
    time.sleep(1 * unit)

def space_between_letter():
    time.sleep(3 * unit)     

def N():
    print('N')
    dash()
    space_between_same_letter()
    dot()

def Y():
    print('Y')
    dash()
    space_between_same_letter()
    dot()
    space_between_same_letter()
    dash()
    space_between_same_letter()
    dash()

def C():
    print('C')
    dash()
    space_between_same_letter()
    dot()
    space_between_same_letter()
    dash()
    space_between_same_letter()
    dot()

def U():
    print('U')
    dot()
    space_between_same_letter()
    dot()
    space_between_same_letter()
    dash()




if __name__ == "__main__":

    N()
    space_between_letter()
    Y()
    space_between_letter()
    C()
    space_between_letter()
    U()
    space_between_letter()
    time.sleep(7 * unit)
    GPIO.cleanup()