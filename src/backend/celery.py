from __future__ import absolute_import, unicode_literals
from celery.schedules import crontab

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
celery_app = Celery('backend')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.autodiscover_tasks()

# 12:30 notification
# celery_app.conf.beat_schedule = {
#     'weekly-email': {
#         'task': 'periodic_task',
#         'schedule': crontab(minute='30', hour='12', day_of_week='6'),
#         'args': (),
#     },
# }
# app.conf.timezone = 'UTC'
