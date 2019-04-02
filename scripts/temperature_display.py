#!/usr/bin/python3

import memcache
import time
import datetime

from Adafruit_LED_Backpack import SevenSegment

segment = SevenSegment.SevenSegment()
segment.begin()

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

lastjacuzzis = [ 0 ]

while True:
    temperatures = mc.get('temperatures')
    try:
        jacuzzi = temperatures['jacuzzi']
    except:
        jacuzzi = 99.9

    segment.clear()
    segment.print_float(jacuzzi, decimal_digits=1, justify_right=False)
    segment.set_colon(False)
    #segment.set_digit_raw(3, 1100011)

    if lastjacuzzis[0] == 0:
       for j in range(1,10):
          for i in [ 65, 34, 65, 34 ]:
             segment.set_digit_raw(3, 99 - i)
             segment.write_display()
             time.sleep(.1)
    elif jacuzzi > lastjacuzzis[0] + 0.025:
       for j in range(1,10):
          for i in [ 1, 2, 64, 32 ]:
             segment.set_digit_raw(3, 99 - i)
             segment.write_display()
             time.sleep(.1)
    elif jacuzzi < lastjacuzzis[0] - 0.025:
       for j in range(1,10):
          for i in [ 32, 64, 2, 1]:
             segment.set_digit_raw(3, 99 - i)
             segment.write_display()
             time.sleep(.1)
    else:
        segment.set_digit_raw(3, 99)
        segment.write_display()
        time.sleep(4)

    lastjacuzzis.append(jacuzzi)
    # compare avec la mesure d'il y environ 140 secondes....
    if len(lastjacuzzis) > 30:
         del  lastjacuzzis[0]

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
