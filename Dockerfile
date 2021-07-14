# pull official base image
FROM python:3

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# install psycopg2
RUN pip install --upgrade pip

# install dependencies
COPY ./service/requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY ./src .

# collect static files
RUN python manage.py collectstatic --noinput

# add and run as non-root user
#RUN adduser -D myuser
#USER myuser

# run gunicorn
#CMD gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT
CMD daphne -b 0.0.0.0 -p $PORT backend.asgi:application
