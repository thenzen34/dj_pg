#!/bin/bash
#heroku container:login
#docker build -t web:latest .
#docker run -d --name django-heroku -e "PORT=8765" -e "DEBUG=1" -p 8007:8765 web:latest
APP_NAME=nameless-fortress-14304

docker build -t registry.heroku.com/$APP_NAME/web .
docker push registry.heroku.com/$APP_NAME/web

#heroku container push -> release
#heroku ps:scale test=1 -a $APP_NAME
heroku container:release -a $APP_NAME web
heroku container:release -a $APP_NAME test

# heroku config:set SECRET_KEY=SOME_SECRET_VALUE -a $APP_NAME
# heroku open -a $APP_NAME

heroku logs  -a $APP_NAME
# heroku addons:create heroku-postgresql:hobby-dev -a $APP_NAME
# heroku run python manage.py makemigrations -a $APP_NAME

#heroku run python manage.py migrate -a $APP_NAME
# heroku run python manage.py createsuperuser -a $APP_NAME
