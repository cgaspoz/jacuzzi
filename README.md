# jacuzzi
Jacuzzi controller

sudo apt-get install memcached

sudo apt-get install python-memcache

sudo apt-get install python3-w1thermsensor

sudo apt-get install influxdb


## Squeezelite
sudo apt-get install squeezelite

sudo apt-get install libflac-dev


sudo vi /etc/default/squeezelite

add SB_EXTRA_ARGS="-a 180"

set gain with

alsamixer


# New install

systemctl restart influxdb
curl https://packages.grafana.com/gpg.key | sudo apt-key add -
vi /etc/apt/sources.list.d/influxdb.list
sudo vi /etc/apt/sources.list.d/influxdb.list
sudo apt-get update
sudo apt-get install grafana
systemctl daemon-reload
sudo systemctl daemon-reload
sudo systemctl start grafana-server
sudo systemctl status grafana-server
sudo systemctl enable grafana-server.service
/etc/init.d/supervisor stop
ps aux
sudo rm /var/log/jacuzzi.*
/etc/init.d/supervisor start
ps aux
less /var/log/jacuzzi.err.log
ls
vi update_influx_phorp.py
./update_influx_phorp.py
vi update_influx_phorp.py
./update_influx_phorp.py
sudo apt-get install python-memcache
vi update_influx_phorp.py
./update_influx_phorp.py
/etc/init.d/supervisor stop
sudo rm /var/log/jacuzzi.*
sudo /etc/init.d/supervisor start
ps aux
less /var/log/jacuzzi.err.log
less /var/log/jacuzzi.out.log
less /var/log/jacuzzi.err.log
exit
cd /var/jacuzzi/
git status
git add scripts/*.py
git status
git add elotouch-calibration/
git status
git commit -m "Upgrade season 2019"
git config --global user.email "jacuzzi@localhost"
git config --global user.name "Jacuzzi"
git commit -m "Upgrade season 2019"
git push
git pull
git push
exit
