#!/usr/bin/python3

# Uses withermsensor from https://github.com/timofurrer/w1thermsensor

from w1thermsensor import W1ThermSensor
import requests
import time
import memcache

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

sensors = {'000004c3902b': 'cabine', '0216006262ff': 'outdoor', '0000055d77fe': 'jacuzzi', '0216005cc3ff': 'primary', '0216007c88ff': 'secondary_in', '0216007d8dff': 'secondary_out'}

sl = requests.Session()
sr = requests.Session()

while True:
    w1 = ''
    temperatures = {}

    for sensor in W1ThermSensor.get_available_sensors():
        temperature = sensor.get_temperature()
        w1 += "temperature,sensor=%s,location=%s value=%.2f\n" % (sensor.id, sensors[sensor.id], temperature)
        temperatures[sensors[sensor.id]] = temperature

    mc.set('temperatures', temperatures)
    sl.post('http://localhost:8086/write?db=jacuzzi', data = w1[:-2])
    sr.post('https://jacuzzi.ga-fl.net:8086/write?db=jacuzzi&u=jacuzzi&p=likeithot', data = w1[:-2])
    time.sleep(60)
