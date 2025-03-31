# syntax=docker/dockerfile:1
FROM ubuntu:22.04

# install app dependencies
RUN apt-get update && apt-get install -y python3 python3-dev python3-pip apache2 apache2-dev build-essential pkg-config default-libmysqlclient-dev
RUN pip install django==3.2.*
RUN pip install mod-wsgi
RUN pip install mysqlclient

# install app
COPY  ./* /WSApp/
COPY  WeatherStation/* /WSApp/WeatherStation/
COPY  WSPro/* /WSApp/WSPro/

# make Django migrations
RUN mkdir ./WSApp/db
RUN chmod 777 ./WSApp/runserver.sh

# setup server 
CMD ./WSApp/runserver.sh

# setup enviroment
ENV PYTHONUNBUFFERED=1

# final configuration
EXPOSE 80
CMD ["/etc/mod_wsgi-express-80/apachectl", "start", "--log-to-terminal", "-D", "FOREGROUND"]
