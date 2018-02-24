#!/usr/bin/python3

import sys
import memcache
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

mc = memcache.Client(['127.0.0.1:11211'], debug=0)

current_milli_time = lambda: int(round(time.time() * 1000))

WMETER = 22 # GPIO pin using BCM numbering
GPIO.setup(WMETER, GPIO.IN)

def convert_state(sensor):
    if sensor == True:
        return 1
    elif sensor == False:
        return 0
    else:
        return sensor

countable = mc.get('countable')

#initialisation on boot
if type(countable) != type(dict()):
    countable = {}

oc=1
ot=current_milli_time()-1

l=0

f = open("/var/jacuzzi/meter/totJin", 'r')
totJin = int(f.readline())
countable['totJin'] = totJin
f.close()

f = open("/var/jacuzzi/meter/totJout", 'r')
totJout = int(f.readline())
countable['totJout'] = totJout
f.close()

f = open("/var/jacuzzi/meter/totLitres", 'r')
totLitres = int(f.readline())
countable['totLitres'] = totLitres
f.close()

print("Read", totJin, totJout, totLitres)
mc.set('countable', countable)

while True :
    c = convert_state(GPIO.input(WMETER))
    t = current_milli_time()
    temperatures = mc.get('temperatures')
    jtemp = temperatures['secondary_in']
    rtemp = temperatures['secondary_out']
    dtemp = rtemp - jtemp   
    # print(t, c, jtemp, rtemp, dtemp)

    if c == 1 and oc == 0:
        dt = t - ot
        print("Rising edge, dt=", dt, "temp aller=", jtemp, "temp retour=", rtemp, "dif=", dtemp)
        if l > 0 and dt > 0:
            lth = 3600000/dt
            ltm =   60000/dt 

            joules = int(dtemp * 4190 )
            power = int(dtemp * lth * 4.19 / 3.6)
            
            if joules > 0 :
                totJin += joules
                countable['totJin'] = totJin
                if l % 100 == 0: # preserve la flash ;)
                    f = open("/var/jacuzzi/meter/totJin", 'w')
                    f.write(str(totJin) + "\n")
                    f.close()
            else:
                totJout -= joules
                countable['totJout'] = totJout
                if l % 100 == 0: # preserve la flash ;)
                    f = open("/var/jacuzzi/meter/totJout", 'w')
                    f.write(str(totJout) + "\n")
                    f.close()

            # print("lth=", lth, "ltm=", ltm, "power=", power, "joules=", joules, "inJ=", totJin, "outJ=", totJout, "totLitres=", totLitres)

        totLitres += 1
        countable['totLitres'] = totLitres
        countable['heatrun'] = 0
        if l % 100 == 0: # preserve la flash ;)
            f = open("/var/jacuzzi/meter/totLitres", 'w')
            f.write(str(totLitres) + "\n")
            f.close()

        mc.set('countable', countable)
        ot = t
        oc = 1
        l += 1

    elif c == 0 and oc == 1:
        print("Falling edge")
        oc = 0

    time.sleep(0.1)
