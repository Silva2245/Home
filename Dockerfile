FROM ubuntu
RUN apt-get update
RUN apt-get full-upgrade -y
RUN apt-get install git -y
RUN apt-get install python3-django -y
RUN apt-get install python3-bs4 -y
RUN apt-get install python3-rsa -y
RUN git clone https://github.com/Silva2245/Home.git
RUN apt-get install neofetch -y
RUN apt-get install net-tools -y
RUN apt-get install openvpn -y
RUN apt-get install openssh-server -y
RUN apt-get install vsftpd -y
RUN apt-get install nmap -y
RUN apt-get install netdiscover -y
