# This is the settings file for travis.

from plugincheck.settings.base import *
from plugincheck.settings_utils import parse_cache_url


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'plugincheck',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
    }
}
