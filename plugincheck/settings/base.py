"""
Django settings for plugincheck project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os

from plugincheck.settings_utils import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='ChangeMe!', type_='str')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default='False', type_='bool')

TEMPLATE_DEBUG = config('DEBUG', default='False', type_='bool')


# Application definition

INSTALLED_APPS = (
    # django contrib apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd party
    'django_browserid',
    'simple_history',

    # local apps
    'plugincheck.base',
    'plugincheck.plugins',

    # more django contrib apps that need to load later
    'django.contrib.admin',   # needs to be after plugincheck.base
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
)

ROOT_URLCONF = 'plugincheck.urls'

WSGI_APPLICATION = 'plugincheck.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


AUTHENTICATION_BACKENDS = (
   'plugincheck.base.auth.OnlyMozillaBackend',
)

BROWSERID_AUDIENCES = [
    'http://localhost:8000',
    'https://plugincheck-dev.herokuapp.com',
    'http://plugincheck-dev.herokuapp.com',
    'https://plugincheck.herokuapp.com']

LOGIN_REDIRECT_URL = '/admin/'

USE_ETAGS = True

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES = {
    'default':  dj_database_url.config()
}

# Parse cache configuration from $CACHE_URL
CACHES = {'default': config('CACHE_URL', default='locmem://', type_='cache_url')}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'plugincheck', 'static'),
)
