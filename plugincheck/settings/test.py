from plugincheck.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = True

SECRET_KEY = 'super-sekret-key-for-testing'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'plugincheck_test',
        'USER': 'rlr',
        'PASSWORD': '',
        'HOST': 'localhost',
    }
}

import dj_database_url
DATABASES = {
	'default': dj_database_url.config(
		default='postgres://rlr:@localhost:5432/plugincheck_test')
}
