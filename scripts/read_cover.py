#!/usr/bin/python3
# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# ADS1115
# This code is designed to work with the ADS1115_I2CADC I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Analog-Digital-Converters?sku=ADS1115_I2CADC#tabs-0-product_tabset-2

import memcache
import time
import RPi.GPIO as GPIO
import datetime
import requests

from ADS1115 import ADS1115
ads1115 = ADS1115()

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

JACUZZI = 24 # GPIO pin using BCM numbering

GPIO.setmode(GPIO.BCM)
GPIO.setup(JACUZZI, GPIO.OUT)
GPIO.output(JACUZZI, GPIO.HIGH)
#GPIO.output(JACUZZI, GPIO.LOW)


mp = 0
cover = "CLOSED"

opensec = 0
closesec = 0

boilerboost = 0
boilerboosttime = 0

export_last_minute = -1

sl = requests.Session()

while True :
    ads1115.set_channel()
    ads1115.config_single_ended()
    time.sleep(0.1)
    adc = ads1115.read_adc()
    cbar = (float(adc['r'])/1622.0-4.0)/20*250
    if cbar < 0:
        cbar = 0
    mp *= 0.95
    mp += cbar * 0.05
    print("%f %f %f os=%i cs=%i boost=%i boosttime=%i" % (cbar,mp,float(adc['r']),opensec,closesec,boilerboost,boilerboosttime))
    if mp > 18:
        closesec = 0
        opensec += 1
        if cover == "CLOSED":
            cover = "OPEN"
            print("Cover open")
            jacuzzi = {'cover': cover}
            mc.set('jacuzzi', jacuzzi)
    elif mp < 18:
        opensec = 0
        closesec += 1
        if cover == "OPEN":
             cover = "CLOSED"
             print("Cover closed")
             jacuzzi = {'cover': cover}
             mc.set('jacuzzi', jacuzzi)

    if opensec > 120 and boilerboost == 0:   # boost des que le convercle est ouvert depuis 2 minutes
        print("Activating Boost")
        GPIO.output(JACUZZI, GPIO.LOW)
        boilerboost = 1
        boilerboosttime = 0

    if boilerboost:
        boilerboosttime += 1


    if boilerboost and closesec > 300 and boilerboosttime > 1800:  # arrete le boost apres 5 minutes de fermetures et au moins 20 minutes de boost
        print("Stopping Boost")
        boilerboost = 0
        GPIO.output(JACUZZI, GPIO.HIGH)

    #GPIO.output(JACUZZI, GPIO.HIGH)

    now = datetime.datetime.now()
    if now.minute != export_last_minute:
        w1 = "ambient,sensor=coverbar value=%.2f\n" % (mp)

        export_last_minute = now.minute
        print("exporting to influx %s" % (w1))
        sl.post('http://localhost:8086/write?db=jacuzzi', data = w1[:-2])
 
    time.sleep(1)
