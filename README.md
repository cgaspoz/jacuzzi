# Installation

## Jacuzzi controller

Enable SPI, I2C, SSH, 1W

    raspi-config

Configure touchscreen

    sudo cp /home/pi/root/usr/share/X11/xorg.conf.d/99-calibration.conf /usr/share/X11/xorg.conf.d/99-calibration.conf

Install dependencies

    sudo apt-get install supervisor python3-memcache python-memcache memcached build-essential python3-dev python3-smbus python3-w1thermsensor vim

Configure supervisor

    sudo ln -s /var/jacuzzi/supervisor/jacuzzi.conf /etc/supervisor/conf.d/

Install Adafruit libraries for the display

    git clone git@github.com:adafruit/Adafruit_Python_GPIO.git
    git clone git@github.com:adafruit/Adafruit_Python_LED_Backpack.git

Correct print statements in Adafruit_Python_GPIO/setup.py (replace print by print() )

    sudo python3 setup.py install
    sudo python setup.py install (really?)

### Install influxdb

    wget -qO- https://repos.influxdata.com/influxdb.key | sudo apt-key add - 
    source /etc/os-release
    test $VERSION_ID = "7" && echo "deb https://repos.influxdata.com/debian wheezy stable" | sudo tee /etc/apt/sources.list.d/influxdb.list test $VERSION_ID = "8" && echo "deb https://repos.influxdata.com/debian jessie stable" | sudo tee /etc/apt/sources.list.d/influxdb.list test $VERSION_ID = "9" && echo "deb https://repos.influxdata.com/debian stretch stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
    sudo apt-get update
    sudo apt-get install influxdb
    sudo systemctl unmask influxdb.service
    sudo systemctl start influxdb
    sudo cp /home/pi/root/etc/influxdb/influxdb.conf /etc/influxdb/influxdb.conf

## Install Grafana

    curl https://packages.grafana.com/gpg.key | sudo apt-key add - 
    vi /etc/apt/sources.list.d/influxdb.list 
    sudo vi /etc/apt/sources.list.d/influxdb.list
    sudo apt-get update
    sudo apt-get install grafana
    sudo systemctl daemon-reload
    sudo systemctl start grafana-server
    sudo systemctl status grafana-server
    sudo systemctl enable grafana-server.service

## Squeezelite
    sudo apt-get install squeezelite libflac-dev

Add `SB_EXTRA_ARGS="-a 180"` at the end of `/etc/default/squeezelite`

Set gain with `alsamixer`
