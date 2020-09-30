FROM ubuntu:18.04
RUN mkdir /code
WORKDIR /code

RUN apt-get update && apt-get install -y --fix-missing \
        python3 \
        python3-pip \
        python3-setuptools \
        python-dev \
        python3-dev \
        build-essential \
        libpq-dev \
        libxml2-dev \
        libxslt1-dev \
        libldap2-dev \
        libsasl2-dev \
        libssl-dev \
        libffi-dev \
        mysql-server \
        libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /code
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /code

RUN chmod +x -R /code/

CMD ["/bin/bash","run.sh"]
