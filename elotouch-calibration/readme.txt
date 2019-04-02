/usr/share/X11/xorg.conf.d/99-calibration.conf
xinput list-props
xinput list-props "EloTouchSystems,Inc Elo TouchSystems 2216 AccuTouch® USB Touchmonitor Interface" | grep Matrix
xinput set-prop "EloTouchSystems,Inc Elo TouchSystems 2216 AccuTouch® USB Touchmonitor Interface" --type=float "Coordinate Transformation Matrix" 1.333984375 0 -0.22265625 0 1 0 0 0 1

https://wiki.archlinux.org/index.php/Talk:Calibrating_Touchscreen
