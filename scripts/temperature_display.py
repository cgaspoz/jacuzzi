#!/usr/bin/python3

import memcache
import time
import datetime

from Adafruit_LED_Backpack import SevenSegment

segment = SevenSegment.SevenSegment()
segment.begin()

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

lastjacuzzis = [ 0 ]

long_avg = -100
short_avg = 0

near_avg = 0
far_avg = 0

# lcd digit pos
#    1
# 32    2
#    64
# 16    4
#    8

while True:
    temperatures = mc.get('temperatures')
    try:
        jacuzzi = temperatures['jacuzzi']
        if long_avg == -100:
           long_avg = jacuzzi
           short_avg = jacuzzi
        else:
           long_avg = long_avg * 0.98 + jacuzzi * 0.02
           short_avg = short_avg * 0.90 + jacuzzi * 0.10

        print("current: %.3f, short_avg: %.3f, long_avg: %.3f, dif %.3f" % (jacuzzi, short_avg, long_avg, short_avg - long_avg))
    except:
        jacuzzi = 99.9


    segment.clear()
    if jacuzzi > 90:
       segment.set_digit_raw(0, 99)
       segment.set_digit_raw(1, 8)
       segment.set_digit_raw(2, 8)
    else:
       segment.print_float(jacuzzi, decimal_digits=1, justify_right=False)
       segment.set_colon(False)
       #segment.set_digit_raw(3, 1100011)

    if near_avg == 0:
       for j in range(1,10):
          for i in [ 65, 34, 65, 34 ]:
             segment.set_digit_raw(3, 99 - i)
             segment.write_display()
             time.sleep(.1)
    elif near_avg > far_avg + 0.025:
       for j in range(1,10):
          for i in [ 1, 2, 64, 32 ]:
             segment.set_digit_raw(3, 99 - i)
             segment.write_display()
             time.sleep(.1)
    elif near_avg < far_avg - 0.025:
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
    # recalcule la moyennes des 10 deniers et des 10 d'avant
    
    if len(lastjacuzzis) >= 20:
        near_avg = 0
        for i in range(10,20):
            near_avg += lastjacuzzis[i]
        near_avg /= 10

        far_avg = 0
        for i in range(0,10):
            far_avg += lastjacuzzis[i]
        far_avg /= 10

        del  lastjacuzzis[0]


    print("near_avg: %.3f, far_avg: %.3f, dif %.3f" % (near_avg, far_avg, near_avg - far_avg))

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
