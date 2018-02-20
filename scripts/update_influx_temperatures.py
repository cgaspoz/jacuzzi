#!/usr/bin/python3

# Uses withermsensor from https://github.com/timofurrer/w1thermsensor

from w1thermsensor import W1ThermSensor
import requests
import time

sensors = {'000004c3902b': 'cabine', '0216006262ff': 'outdoor', '0000055d77fe': 'jacuzzi', '0216005cc3ff': 'primary', '0216007c88ff': 'secondary_in', '0216007d8dff': 'secondary_out'}

while True:
    w1 = ''

    for sensor in W1ThermSensor.get_available_sensors():
        w1 += "temperature,sensor=%s,location=%s value=%.2f\n" % (sensor.id, sensors[sensor.id], sensor.get_temperature())

    requests.post('http://localhost:8086/write?db=jacuzzi', data = w1[:-2])
    print(w1)
    time.sleep(60)
