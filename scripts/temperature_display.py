#!/usr/bin/python3

import memcache
import time
import datetime

from Adafruit_LED_Backpack import SevenSegment

segment = SevenSegment.SevenSegment()
segment.begin()

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

while True:
    temperatures = mc.get('temperatures')
    try:
        jacuzzi = temperatures['jacuzzi']
    except:
        jacuzzi = 99.9

    segment.clear()
    segment.print_float(jacuzzi, decimal_digits=1, justify_right=False)
    segment.set_digit_raw(3, 1100011)
    segment.set_colon(False)
    segment.write_display()
    time.sleep(5)

    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    segment.clear()
    segment.print_float(hour + minute * 0.01)
    segment.set_colon(True)
    segment.write_display()
    time.sleep(1)
    segment.set_colon(False)
    segment.write_display()
    time.sleep(1)
    segment.set_colon(True)
    segment.write_display()
    time.sleep(1)
