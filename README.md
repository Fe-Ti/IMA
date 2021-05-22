# IMA

Very simple messaging app, which even does not have "create chat" and "register" buttons.
But you can authenticate [*giggles*].

## Intallation
#### You need:
* Python3 pip
* Apache2
* Libapache2-mod-wsgi-py3 (or whatever thing which provides mod_wsgi for python 3)

On Debian|Devuan (may be outdated commands):
```sh
apt-get update
apt-get install python3-pip apache2 libapache2-mod-wsgi-py3
```
#### Process
Install virtualenv
```sh
sudo pip3 install virtualenv # I mean as root
```
Make virtual environment in project dir
```sh
virtualenv imaenv
```
Activate virtual environment
```sh
source imaenv/bin/activate
```
Install Django
```sh
pip3 install django
```
Setup the project
```sh
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py collectstatic
```
Exit virtual environment
```sh
deactivate
```
Then configure apache2 (as in included config file) and set the right permissions.
```sh
# as root
chmod 664 ${PATH_TO_DB}/db.sqlite3
chown www-data:www-data ${PATH_TO_DB}/db.sqlite3
chown www-data:www-data ${PATH_TO_DB}/

# then restart apache2
```
Also you may want to change the secret key in settings.py
