# Dockerfile
FROM quay.io/aptible/ubuntu:14.04

# Basic dependencies
RUN apt-install update
RUN apt-install upgrade -y
RUN apt-install python3.5 build-essential python3.5-dev python3-setuptools
RUN apt-install libxml2-dev libxslt1-dev python3.5-dev python3-pip
RUN apt-get install -y python3-pip  
RUN apt-install libffi-dev libssl-dev

RUN echo '####################'
# RUN pip3 --version
RUN python3 --version
RUN echo '####################'


# PostgreSQL dev headers and client (uncomment if you use PostgreSQL)
RUN apt-install libpq-dev postgresql-client-9.3 postgresql-contrib-9.3

RUN apt-get autoremove
RUN apt-get clean

# Add requirements.txt ONLY, then run pip install, so that Docker cache won't
# bust when changes are made to other repo files
RUN pip3 install requests[security]
ADD requirements.txt /app/
WORKDIR /app

RUN pip3 install -r requirements.txt

# Add repo contents to image
ADD . /app/

ENV PORT 3000
EXPOSE 3000
