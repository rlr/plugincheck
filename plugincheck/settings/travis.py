# This is the settings file for travis.

from plugincheck.settings.base import *


DEBUG = True
TEMPLATE_DEBUG = True

SECRET_KEY = 'travis-doesnt-keep-secrets'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'plugincheck',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
    }
}
