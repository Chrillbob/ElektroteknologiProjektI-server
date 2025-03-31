python3 ./WSApp/manage.py makemigrations WeatherStation
python3 ./WSApp/manage.py migrate
/etc/mod_wsgi-express-80/apachectl start --log-to-terminal -D FOREGROUND