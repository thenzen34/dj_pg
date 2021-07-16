migrate: python manage.py migrate
collectstatic: python manage.py collectstatic --noinput
web: daphne -b 0.0.0.0 -p $PORT backend.asgi:application
channels: python manage.py runworker channels --settings=backend.settings
celery: celery -A backend worker -l INFO
test: echo hello
