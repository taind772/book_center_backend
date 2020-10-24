FROM python:alpine

COPY ./requirements.txt requirements.txt

RUN apk update && apk upgrade

RUN apk add --no-cache mariadb-connector-c-dev bash &&\
    apk add --upgrade --no-cache --virtual .tmp build-base mariadb-dev\
    && pip install -r /requirements.txt\
    && apk del .tmp

RUN mkdir -p /app
COPY ./app /app
WORKDIR /app

COPY ./scripts /scripts
RUN chmod +x /scripts/*

RUN adduser -D ndt
USER ndt