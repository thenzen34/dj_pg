from django.http import HttpRequest

from .settings import *

if DEBUG:
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
    INSTALLED_APPS.append('debug_toolbar')
    INTERNAL_IPS = ('*',)  # ('127.0.0.1', 'localhost')


    def show_toolbar(request):
        """

        :type request: HttpRequest
        """
        return not request.is_ajax() and request.user and request.user.username == "admin"


    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': show_toolbar,
        # Rest of config
    }

