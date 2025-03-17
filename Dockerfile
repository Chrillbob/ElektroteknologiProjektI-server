# syntax=docker/dockerfile:1
FROM ubuntu:22.04

# install app dependencies
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install django==3.2.*

# install app
COPY  .* /

# final configuration
EXPOSE 80
CMD ["python3", "manage.py", "runserver"]