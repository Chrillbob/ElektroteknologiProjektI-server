python3 ./WSApp/manage.py makemigrations WeatherStation
python3 ./WSApp/manage.py migrate
python3 ./WSApp/manage.py runmodwsgi --setup-only --port=80 --user www-data --group www-data --server-root=/etc/mod_wsgi-express-80
/etc/mod_wsgi-express-80/apachectl start --log-to-terminal -D FOREGROUND