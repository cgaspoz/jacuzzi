#!/usr/bin/python3

import smbus
import time

bus = smbus.SMBus(1)

while True:
    block = bus.read_i2c_block_data(0x48, 0x00, 2)
    byte = bus.read_byte_data(0x48, 0)
    print("Block: %s | Byte: %s" % (block, byte))
    time.sleep(1)
