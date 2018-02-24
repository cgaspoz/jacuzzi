#!/usr/bin/python3

import requests
import time
import memcache

mc = memcache.Client(['127.0.0.1:11211'], debug=0)


while True:
    countable = mc.get('countable')

    if type(countable) == type(dict()):
        c = "water,sensor=liters value=%s\nwater,sensor=joules_in value=%s\nwater,sensor=joules_out value=%s" % (countable['totLitres'], countable['totJin'], countable['totJout'])

    requests.post('http://localhost:8086/write?db=jacuzzi', data = c)
    time.sleep(60)
