FROM python:3.8

RUN apt-get update

# Install supervisord
RUN apt-get install --no-install-recommends -y wget nano curl supervisor make g++ bzip2 software-properties-common mariadb-server default-libmysqlclient-dev python-dev

# Config supervisor
RUN mkdir -p /tmp/logs
RUN mkdir -p /var/log/supervisor
RUN rm -rf /var/lib/apt/lists/*

ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 8080 8000 9001

CMD supervisord


