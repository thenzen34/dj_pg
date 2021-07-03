# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
import os

from .settings import BASE_DIR

BACKEND_DB_ENGINE = os.getenv('BACKEND_DB_ENGINE')
if 'sqlite3' == BACKEND_DB_ENGINE:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.{0}'.format(BACKEND_DB_ENGINE),
            'NAME': '{0}/{1}'.format(BASE_DIR, os.getenv('BACKEND_DB_NAME')),
            'TEST': {
                # 'NAME': BASE_DIR / os.getenv('BACKEND_DB_NAME'),
            },
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.{0}'.format(BACKEND_DB_ENGINE),
            'NAME': os.getenv('BACKEND_DB_NAME'),
            'USER': os.getenv('BACKEND_DB_USER'),
            'PASSWORD': os.getenv('BACKEND_DB_PASSWORD'),
            'HOST': os.getenv('BACKEND_DB_HOST'),
            'PORT': os.getenv('BACKEND_DB_PORT'),
        }
    }