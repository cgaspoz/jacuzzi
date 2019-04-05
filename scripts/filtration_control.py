#!/usr/bin/python3

import sys
import memcache
import time
import datetime
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
FILTRATION = 18 # GPIO pin using BCM numbering
GPIO.setup(FILTRATION, GPIO.OUT)
GPIO.output(FILTRATION, GPIO.HIGH)

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

filtration_stopped = GPIO.input(FILTRATION)
filtration_heat_run = False
filtration_freeze_run = False
filtration_freeze_start = datetime.datetime.now() - datetime.timedelta(minutes=120)
filtration_manual_run = False
filtration_manual_start = datetime.datetime.now()
filtration_auto_run = False
filtration_auto_stop = datetime.datetime.now()
filtration_start = datetime.datetime.now()
filtration_duration = 0
filtration_minimum = 7200

print('Filtration daemon starting...\nCurrent state: %s' % filtration_stopped)


def filtration_running():
    if filtration_stopped:
        return False
    else:
        return True


while True:
    filtration_stopped = GPIO.input(FILTRATION)

    temperatures = mc.get('temperatures')
    if type(temperatures) == type(dict()):
        primary = temperatures['primary']
        secondary = temperatures['secondary_in']
    else:
        # We have no temperatures, we define safety values (we run the filtration)
        primary = 46
        secondary = 0

    filtration = mc.get('filtration')
    if type(filtration) == type(dict()):
        filtration_manual_run = filtration['manual_run']
        filtration_manual_start = filtration['manual_start']
    else:
        # We define defaults
        filtration_manual_run = False
        filtration_manual_start = datetime.datetime.now()

    if primary > 45 and not filtration_heat_run:
        filtration_heat_run = True
        print('Starting heat filtration')
    elif primary <= 45 and filtration_heat_run:
        filtration_heat_run = False
        print('Stopping heat filtration')

    if secondary < 2 and filtration_freeze_start < datetime.datetime.now() - datetime.timedelta(minutes=120) and not filtration_freeze_run:
        filtration_freeze_run = True
        filtration_freeze_start = datetime.datetime.now()
        print('Starting freezing prevention for 3 min')
    elif filtration_freeze_start < datetime.datetime.now() - datetime.timedelta(minutes=5) and filtration_freeze_run:
        filtration_freeze_run = False
        print('Stopping freezing prevention')

    if filtration_manual_run and filtration_stopped:
        filtration_manual_start = datetime.datetime.now()
        print('Starting manual filtration')
    elif filtration_manual_run and filtration_manual_start < datetime.datetime.now() - datetime.timedelta(minutes=240):
        filtration_manual_run = False
        print('Stopping manual filtration')

    if not filtration_auto_run and datetime.datetime.now().time() > datetime.time(21, 0, 0, 0) and filtration_duration < filtration_minimum:
        filtration_auto_run = True
        filtration_auto_stop = datetime.datetime.now() + datetime.timedelta(seconds=filtration_minimum-filtration_duration)

    if filtration_auto_run and datetime.datetime.now() > filtration_auto_stop:
        filtration_auto_run = False

    if filtration_duration > 0 and datetime.time(1, 0, 0, 0) < datetime.datetime.now().time() < datetime.time(1, 1, 0, 0):
        # We reset the duration
        filtration_duration = 0

    if (filtration_heat_run or filtration_freeze_run or filtration_manual_run or filtration_auto_run) and filtration_stopped:
        # Starting filtration
        filtration_start = datetime.datetime.now()
        GPIO.output(FILTRATION, GPIO.LOW)
    elif not filtration_heat_run and not filtration_freeze_run and not filtration_manual_run and not filtration_auto_run and not filtration_stopped:
        # Stopping filtration
        duration = datetime.datetime.now() - filtration_start
        filtration_duration += duration.seconds
        GPIO.output(FILTRATION, GPIO.HIGH)

    filtration = {'manual_start': filtration_manual_start, 'manual_run': filtration_manual_run, 'running': filtration_running(), 'duration': filtration_duration}
    mc.set('filtration', filtration)
    #print('HEAT: ', filtration_heat_run, ' | FREEZE: ', filtration_freeze_run, ' | MANUAL: ', filtration_manual_run)

    time.sleep(10)
