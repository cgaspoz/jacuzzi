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

Using username "pi".
pi@192.168.5.14's password:
Linux jacuzzi 4.14.98-v7+ #1200 SMP Tue Feb 12 20:27:48 GMT 2019 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Tue Apr  2 23:04:35 2019 from 192.168.5.206
pi@jacuzzi:~ $ less .bash_history
pi@jacuzzi:~ $
pi@jacuzzi:~ $ less .bash_history
pi@jacuzzi:~ $ cp .bash_history install
pi@jacuzzi:~ $ vi install
pi@jacuzzi:~ $ sudo apt-get install squeezelite
Lecture des listes de paquets... Fait
Construction de l'arbre des dépendances
Lecture des informations d'état... Fait
Le paquet suivant a été installé automatiquement et n'est plus nécessaire :
  realpath
Veuillez utiliser « sudo apt autoremove » pour le supprimer.
Les NOUVEAUX paquets suivants seront installés :
  squeezelite
0 mis à jour, 1 nouvellement installés, 0 à enlever et 0 non mis à jour.
Il est nécessaire de prendre 67.8 ko dans les archives.
Après cette opération, 172 ko d'espace disque supplémentaires seront utilisés.
Réception de:1 http://debian.anexia.at/raspbian/raspbian stretch/main armhf squeezelite armhf 1.8-4 [67.8 kB]
67.8 ko réceptionnés en 0s (120 ko/s)
Sélection du paquet squeezelite précédemment désélectionné.
(Lecture de la base de données... 137539 fichiers et répertoires déjà installés.)
Préparation du dépaquetage de .../squeezelite_1.8-4_armhf.deb ...
Dépaquetage de squeezelite (1.8-4) ...
Traitement des actions différées (« triggers ») pour systemd (232-25+deb9u9) ...
Traitement des actions différées (« triggers ») pour man-db (2.7.6.1-2) ...
Paramétrage de squeezelite (1.8-4) ...
Traitement des actions différées (« triggers ») pour systemd (232-25+deb9u9) ...
pi@jacuzzi:~ $
pi@jacuzzi:~ $ sudo apt-get install libflac-dev
Lecture des listes de paquets... Fait
Construction de l'arbre des dépendances
Lecture des informations d'état... Fait
Le paquet suivant a été installé automatiquement et n'est plus nécessaire :
  realpath
Veuillez utiliser « sudo apt autoremove » pour le supprimer.
The following additional packages will be installed:
  libogg-dev
Les NOUVEAUX paquets suivants seront installés :
  libflac-dev libogg-dev
0 mis à jour, 2 nouvellement installés, 0 à enlever et 0 non mis à jour.
Il est nécessaire de prendre 389 ko dans les archives.
Après cette opération, 1'182 ko d'espace disque supplémentaires seront utilisés.
Souhaitez-vous continuer ? [O/n]
Réception de:1 http://debian.anexia.at/raspbian/raspbian stretch/main armhf libogg-dev armhf 1.3.2-1 [195 kB]
Réception de:2 http://debian.anexia.at/raspbian/raspbian stretch/main armhf libflac-dev armhf 1.3.2-1 [193 kB]
389 ko réceptionnés en 0s (488 ko/s)
Sélection du paquet libogg-dev:armhf précédemment désélectionné.
(Lecture de la base de données... 137547 fichiers et répertoires déjà installés.)
Préparation du dépaquetage de .../libogg-dev_1.3.2-1_armhf.deb ...
Dépaquetage de libogg-dev:armhf (1.3.2-1) ...
Sélection du paquet libflac-dev:armhf précédemment désélectionné.
Préparation du dépaquetage de .../libflac-dev_1.3.2-1_armhf.deb ...
Dépaquetage de libflac-dev:armhf (1.3.2-1) ...
Paramétrage de libogg-dev:armhf (1.3.2-1) ...
Paramétrage de libflac-dev:armhf (1.3.2-1) ...
pi@jacuzzi:~ $ sudo vi /etc/default/squeezelite
pi@jacuzzi:~ $ alsamixer
pi@jacuzzi:~ $ alsamixer
pi@jacuzzi:~ $ /etc/init.d/squeezelite restart
[....] Restarting squeezelite (via systemctl): squeezelite.service==== AUTHENTICATING FOR org.freedesktop.systemd1.manage-units ===
Authentification requise pour redémarrer « squeezelite.service ».
Multiple identities can be used for authentication:
 1.  ,,, (pi)
 2.  root
Choose identity to authenticate as (1-2): 1
Password:
==== AUTHENTICATION COMPLETE ===
. ok
pi@jacuzzi:~ $ sudo /etc/init.d/squeezelite restart
[ ok ] Restarting squeezelite (via systemctl): squeezelite.service.
pi@jacuzzi:~ $ vi install
raspi-config
sudo cp /home/pi/root/usr/share/X11/xorg.conf.d/99-calibration.conf /usr/share/X11/xorg.conf.d/99-calibration.conf
sudo apt-get install supervisor
sudo ln -s /var/jacuzzi/supervisor/jacuzzi.conf /etc/supervisor/conf.d/
sudo apt-get install python3-memcache
sudo apt-get install memcached
git clone git@github.com:adafruit/Adafruit_Python_LED_Backpack.git
sudo apt-get install build-essential python3-dev
sudo apt-get install python3-smbus
sudo python3 setup.py install
sudo python setup.py install
git clone git@github.com:adafruit/Adafruit_Python_GPIO.git
sudo apt-get install vim
sudo python3 setup.py install
cd Adafruit_Python_LED_Backpack/
sudo python3 setup.py install
sudo apt-get install python3-w1thermsensor
wget -qO- https://repos.influxdata.com/influxdb.key | sudo apt-key add -
source /etc/os-release
test $VERSION_ID = "7" && echo "deb https://repos.influxdata.com/debian wheezy stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
test $VERSION_ID = "8" && echo "deb https://repos.influxdata.com/debian jessie stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
test $VERSION_ID = "9" && echo "deb https://repos.influxdata.com/debian stretch stable" | sudo tee /etc/apt/sources.list.d/influxdb.list
sudo apt-get update
sudo apt-get install influxdb
sudo systemctl unmask influxdb.service
sudo systemctl start influxdb
sudo cp /home/pi/root/etc/influxdb/influxdb.conf /etc/influxdb/influxdb.conf
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
sudo apt-get install python-memcache
