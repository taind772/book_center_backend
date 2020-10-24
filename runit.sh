#!/bin/sh

#clean cache, command it in deploy

rm -rf ./app/*/__pycache__
rm -rf ./app/*/migrations

#remove test database, command it in deploy

rm -rf ./mysql/database/*

#clean docker -- just for me, dont uncommand them if u have any other docker data

# docker container prune -f
# docker volume prune -f
# docker system prune -f
# docker image rm backend_app

docker-compose up