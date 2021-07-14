#!/bin/bash
#heroku container:login
#docker build -t web:latest .
#docker run -d --name django-heroku -e "PORT=8765" -e "DEBUG=1" -p 8007:8765 web:latest
# TODO APP_NAME=nameless-fortress-14304

docker build -t registry.heroku.com/nameless-fortress-14304/web .
docker push registry.heroku.com/nameless-fortress-14304/web
heroku container:release -a nameless-fortress-14304 web

# heroku config:set SECRET_KEY=SOME_SECRET_VALUE -a nameless-fortress-14304
heroku open -a nameless-fortress-14304
# heroku addons:create heroku-postgresql:hobby-dev -a nameless-fortress-14304
# heroku run python manage.py makemigrations -a nameless-fortress-14304

#heroku run python manage.py migrate -a nameless-fortress-14304
# heroku run python manage.py createsuperuser -a nameless-fortress-14304
