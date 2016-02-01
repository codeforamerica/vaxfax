# Dockerfile
FROM quay.io/aptible/ubuntu:14.04

# Basic dependencies
RUN apt-install build-essential python3-dev python-setuptools
RUN apt-install libxml2-dev libxslt1-dev python3-dev python3-pip
RUN apt-install libffi-dev libssl-dev

RUN echo '####################'
RUN pip --version
RUN python --version
RUN echo '####################'


# PostgreSQL dev headers and client (uncomment if you use PostgreSQL)
RUN apt-install libpq-dev postgresql-client-9.3 postgresql-contrib-9.3

RUN easy_install pip
RUN pip install requests[security]

# Add requirements.txt ONLY, then run pip install, so that Docker cache won't
# bust when changes are made to other repo files
ADD requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt

# Add repo contents to image
ADD . /app/

ENV PORT 3000
EXPOSE 3000
