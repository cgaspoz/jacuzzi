#!/bin/sh

echo desactivating screen blanking

export DISPLAY=:0.0
xset s off
xset s noblank
xset -dpms

