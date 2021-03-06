#!/usr/bin/python3

# Uses withermsensor from https://github.com/timofurrer/w1thermsensor

from w1thermsensor import W1ThermSensor
import requests
import time
import memcache
import datetime

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

sensors = {'000004c3902b': 'cabine', '0216006262ff': 'outdoor', '0000055d77fe': 'jacuzzi', '0216005cc3ff': 'primary', '0216007c88ff': 'secondary_in', '0216007d8dff': 'secondary_out'}

sl = requests.Session()
sr = requests.Session()

export_last_minute = -1

while True:
    w1 = ''
    temperatures = {}

    for sensor in W1ThermSensor.get_available_sensors():
        temperature = sensor.get_temperature()
        if temperature < 84.00:
            w1 += "temperature,sensor=%s,location=%s value=%.2f\n" % (sensor.id, sensors[sensor.id], temperature)
            temperatures[sensors[sensor.id]] = temperature
        else:
            print("bad reading of %s" % (sensors[sensor.id]))

    now = datetime.datetime.now()
    print("%02i:%02i:%02i" % (now.hour, now.minute, now.second))
    print(temperatures)
    print(w1[:-2])
    mc.set('temperatures', temperatures)
    if now.minute != export_last_minute:
        export_last_minute = now.minute
        print("exporting to influx")
        sl.post('http://localhost:8086/write?db=jacuzzi', data = w1[:-2])
        #sr.post('https://jacuzzi.ga-fl.net:8086/write?db=jacuzzi&u=jacuzzi&p=likeithot', data = w1[:-2])

    time.sleep(1)
