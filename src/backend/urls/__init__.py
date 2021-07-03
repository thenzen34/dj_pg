from .urls import *

from .debug_toolbar import urlpatterns as debug_urlpatterns
from django.conf import settings

if settings.DEBUG:
    urlpatterns += debug_urlpatterns
