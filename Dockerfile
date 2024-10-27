FROM ubuntu
RUN apt-get update
RUN apt-get install python3 python3-django python3-psutil python3-bs4 -y
