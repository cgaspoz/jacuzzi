#!/usr/bin/python3
# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# ADS1115
# This code is designed to work with the ADS1115_I2CADC I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Analog-Digital-Converters?sku=ADS1115_I2CADC#tabs-0-product_tabset-2

import RPi.GPIO as GPIO

JACUZZI = 24 # GPIO pin using BCM numbering

GPIO.setmode(GPIO.BCM)
GPIO.setup(JACUZZI, GPIO.OUT)
GPIO.output(JACUZZI, GPIO.HIGH)

print("De-Activating Boost")
GPIO.output(JACUZZI, GPIO.HIGH)

