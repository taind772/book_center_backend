#!/bin/sh

#clean cache, comment it in deploy

rm -rf ./app/*/__pycache__
rm -rf ./app/*/migrations

#remove test database, comment it in deploy

rm -rf ./mysql/database
rm -rf ./app/*DB

#clean docker -- just for me, dont uncomment them if u have any other docker data

# docker container prune -f
# docker volume prune -f
# docker system prune -f
# docker image rm backend_app

docker-compose up --build