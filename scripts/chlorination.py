#!/usr/bin/python3

import sys
import memcache
import time
import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
CHLORINATION = 25 # GPIO pin using BCM numbering
GPIO.setup(CHLORINATION, GPIO.OUT)
GPIO.output(CHLORINATION, GPIO.HIGH)

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

chlorination_stopped = GPIO.input(CHLORINATION)
chlorination_start = datetime.datetime.now() - datetime.timedelta(minutes=60)

print('Chlorination daemon starting...\nCurrent state: %s' % chlorination_stopped)


while True:
    water = mc.get('water')
    if type(water) == type(dict()):
        ph = water['pH']
        orp = water['ORP']
    else:
        ph = None
        orp = None

    temperature = mc.get('temperatures')
    if type(temperature) == type(dict()):
        jacuzzi = temperature['jacuzzi']
    else:
        jacuzzi = 37.1

    filtration = mc.get('filtration')
    if type(filtration) == type(dict()):
        filtration_running = filtration['running']
    else:
        filtration_running = False

    chlorination_stopped = GPIO.input(CHLORINATION)

    if orp:
        if float(orp) < 650 and filtration_running and chlorination_stopped:
            # We start chlorination for 10 minutes
            GPIO.output(CHLORINATION, GPIO.LOW)
            chlorination_start = datetime.datetime.now()
            print("Starting chlorination for 10 min")
    else:
        print("Unable to read ORP measurement")

    if not chlorination_stopped and chlorination_start < datetime.datetime.now() - datetime.timedelta(minutes=10):
        GPIO.output(CHLORINATION, GPIO.HIGH)
        print("Stopping chlorination after 10 min")
        
    time.sleep(10)
