# -*- coding: utf-8 -*-
import lirc
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# LED_1_PIN 
PIN_1 = 16                                    
GPIO.setup(PIN_1, GPIO.OUT)

# LED_2_PIN 
PIN_2 = 15                                 
GPIO.setup(PIN_2, GPIO.OUT)

sockid = lirc.init('LED', '.lircrc', verbose = True)

try:
    while True:
        inf = lirc.nextcode()

        if len(inf) == 0:
            continue
        
        if inf[0] == 'on_1':
            GPIO.output(PIN_1, GPIO.HIGH)
            print("LED_1_ON")

        elif inf[0] == 'off_1':
            print("LED_1_OFF")
            GPIO.output(PIN_1, GPIO.LOW)

        elif inf[0] == 'on_2':
            print("LED_2_ON")
            GPIO.output(PIN_2, GPIO.HIGH)

        elif inf[0] == 'off_2':
            print("LED_2_OFF")
            GPIO.output(PIN_2, GPIO.LOW)


except KeyboardInterrupt:
    print('stop')

finally:
    GPIO.cleanup()
    lirc.deinit()