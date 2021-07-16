#!/bin/bash
APP_NAME=nameless-fortress-14304

git push origin main
git push heroku main

heroku ps:scale web=1 -a $APP_NAME
heroku ps:scale test=1 -a $APP_NAME
heroku ps:scale worker=1 -a $APP_NAME
heroku ps:scale celery=1 -a $APP_NAME

heroku logs  -a $APP_NAME
