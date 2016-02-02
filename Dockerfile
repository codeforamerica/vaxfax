# Dockerfile
FROM quay.io/aptible/ubuntu:14.04

RUN rm /bin/sh && ln -s /bin/bash /bin/sh
ENV PYTHONIOENCODING UTF-8
ENV SHELL /bin/bash

# Basic dependencies
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-install python3 build-essential python3-dev python3-setuptools
RUN apt-install libxml2-dev libxslt1-dev python3-dev python3-pip
RUN apt-get install -y python3-pip
RUN apt-install libffi-dev libssl-dev

RUN echo '####################'
RUN pip3 --version
RUN python3 --version
RUN pip3 install --upgrade setuptools
RUN apt-get update
RUN apt-get install -y wget
RUN echo '####################'

# Get pyphaxio
RUN wget https://pypi.python.org/packages/source/p/pyphaxio/pyphaxio-0.10.tar.gz \
 && tar -xf pyphaxio-0.10.tar.gz \
 && pushd pyphaxio-0.10 \
 && echo > README.rst \
 && python3 setup.py install \
 && rm -r /pyphaxio-0.10{,.tar.gz}

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
