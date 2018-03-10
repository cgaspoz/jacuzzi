#!/usr/bin/python3

import memcache
import datetime

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

filtration = mc.get('filtration')

if filtration['manual_run'] == True:
    filtration['manual_run'] = False
else:
    filtration['manual_run'] = True
    filtration['manual_start'] = datetime.datetime.now()

mc.set('filtration', filtration)

print(filtration)
