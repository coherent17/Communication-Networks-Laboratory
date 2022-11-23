# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop
import Adafruit_DHT

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

''' start of you code '''
PIN = 16
GPIO.setup(PIN, GPIO.OUT)
GPIO.output(PIN, False) 
''' end of you code '''

# Setup DHT11 
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }

sensor = sensor_args['11']
gpio = 4


def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Received: {cmd}'.format(cmd = command))

    if 'on' in command:
        print("LED is on")
        GPIO.output(PIN, GPIO.HIGH)
        telegram_bot.sendMessage(chat_id, 'Turned on the light')
    
    elif 'off' in command:
        print("LED is off")
        GPIO.output(PIN, GPIO.LOW)
        telegram_bot.sendMessage(chat_id, 'Turned off the light')

    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    humidity = str(humidity)
    temperature = str(temperature)

    if  'humidity' in command:
        telegram_bot.sendMessage(chat_id, 'The current humidity is ' + humidity + ' %')
  

    elif 'temperature' in command:
        telegram_bot.sendMessage(chat_id, 'The current temperature is ' + temperature + ' *C')



telegram_bot = telepot.Bot('5962907283:AAG12Qa_mD0Nm3xZ4RVoWVtE51ToRfHukMo')
print(telegram_bot.getMe())

MessageLoop(telegram_bot, action).run_as_thread()
print('Send the command to turn on or off the light...')

while True:
    time.sleep(3)