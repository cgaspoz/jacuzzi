#!/usr/bin/python3

import memcache
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

COVER = 17 # GPIO pin using BCM numbering
JACUZZI = 23 # GPIO pin using BCM numbering

GPIO.setup(COVER, GPIO.IN)
GPIO.setup(JACUZZI, GPIO.OUT)
GPIO.output(JACUZZI, GPIO.HIGH)

def cover_state(cover_closed):
    if cover_closed:
        return "CLOSED"
    else:
        return "OPEN"

def light_state(jacuzzi_off):
    if jacuzzi_off:
        return "OFF"
    else:
        return "ON"

while True :
    cover_closed = GPIO.input(COVER)
    jacuzzi_off = GPIO.input(JACUZZI)

    if not cover_closed and jacuzzi_off:
       GPIO.output(JACUZZI, GPIO.LOW)
    elif cover_closed and not jacuzzi_off:
       GPIO.output(JACUZZI, GPIO.HIGH)

    jacuzzi = {'cover': cover_state(cover_closed), 'lights': light_state(jacuzzi_off)}
    mc.set('jacuzzi', jacuzzi)
    time.sleep(0.5)
