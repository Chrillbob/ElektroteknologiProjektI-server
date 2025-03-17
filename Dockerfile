# syntax=docker/dockerfile:1
FROM ubuntu:22.04

# install app dependencies
RUN apt-get update && apt-get install -y python3 python3-pip apache2 apache2-dev
RUN pip install django==3.2.*
RUN pip install mod-wsgi

# install app
COPY  ./* /WSApp
COPY  WeatherStation/* /WSApp/WeatherStation/
COPY  WeatherStation/migrations/* /WSApp/WeatherStation/migrations/
COPY  WSPro/* /WSApp/WSPro/

# setup server 
RUN python3 ./WSApp/manage.py runmodwsgi --setup-only --port=80 --user www-data --group www-data --server-root=/etc/mod_wsgi-express-80

# setup enviroment
ENV PYTHONUNBUFFERED=1

# final configuration
EXPOSE 80
CMD ["/etc/mod_wsgi-express-80/apachectl", "start", "--log-to-terminal", "-D", "FOREGROUND"]
