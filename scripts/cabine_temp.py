#!/usr/bin/python3

import memcache
import time
import datetime
import RPi.GPIO as GPIO
import datetime

CABINE = 23 # GPIO pin using BCM numbering

GPIO.setmode(GPIO.BCM)
GPIO.setup(CABINE, GPIO.OUT)
GPIO.output(CABINE, GPIO.HIGH)
time.sleep(1)
GPIO.output(CABINE, GPIO.LOW)
time.sleep(3)
GPIO.output(CABINE, GPIO.HIGH)
time.sleep(1)

last = 0
closed = 600

last_cabine = 0
last_cover = "CLOSED"
last_sec = 0
cover = 0

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

while True:
    temperatures = mc.get('temperatures')
    jacuzzi = mc.get('jacuzzi')
    try:
        cabine = temperatures['cabine']
        sec = temperatures['secondary_out']
        #cover = jacuzzi['cover']
        last_cabine = cabine
        #last_cover = cover
        last_sec = sec
    except:
        cabine = last_cabine
        cover = last_cover
        sec = last_sec
        print("could not read, using previous")

    cover = "OPEN"

    print("cabine: %.3f sec: %.3f cover: %s closed_s: %i" % (cabine,sec,cover,closed))
    if cover == "OPEN" or closed < 600:
        if cover == "OPEN":
            closed = 0
        if cabine < 26 and sec > 40:
            if last == 0:
                last = 1
                print("Starting heater")
                GPIO.output(CABINE, GPIO.LOW)
        if cabine > 28 or sec < 38: 
            if last == 1:
                last = 0
                print("Stoping heater")
                GPIO.output(CABINE, GPIO.HIGH)
    else:
        closed += 5
        if last == 1:
            last = 0
            print("Stopping heater")
            GPIO.output(CABINE, GPIO.HIGH)

    time.sleep(5)
