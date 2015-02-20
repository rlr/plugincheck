# This is the settings file for travis.

from plugincheck.settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'plugincheck',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
    }
}
