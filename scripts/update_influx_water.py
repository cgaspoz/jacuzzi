#!/usr/bin/python3

import requests
import time
import memcache

mc = memcache.Client(['127.0.0.1:11211'], debug=0)


while True:
    values = ""

    countable = mc.get('countable')
    if type(countable) == type(dict()):
        values = "water,sensor=liters value=%s\nwater,sensor=joules_in value=%s\nwater,sensor=joules_out value=%s" % (countable['totLitres'], countable['totJin'], countable['totJout'])

    filtration = mc.get('filtration')
    if type(filtration) == type(dict()):
        if values != "":
            values += "\n"
        if filtration['running'] == True:
            value = 1
        else:
            value = 0
        values += "water,sensor=filtration value=%s" % value

    jacuzzi = mc.get('jacuzzi')
    # {'cover': OPEN/CLOSED, 'lights': ON/OFF}
    if type(jacuzzi) == type(dict()):
        if values != "":
            values += "\n"
        if jacuzzi['cover'] == "OPEN":
            jacuzzi_int = 1
        else:
            jacuzzi_int = 0

        values += "ambient,sensor=cover value=\"%s\"\nambient,sensor=lights value=\"%s\"\nambient,sensor=cover_int value=%s" % (jacuzzi['cover'], jacuzzi['lights'], jacuzzi_int)

    requests.post('http://localhost:8086/write?db=jacuzzi', data = values)
    requests.post('https://jacuzzi.ga-fl.net:8086/write?db=jacuzzi&u=jacuzzi&p=likeithot', data = values)
    print(values)
    time.sleep(60)
