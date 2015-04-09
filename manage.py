#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    # If we're running tests, then we pull from
    # DJANGO_TEST_SETTINGS_MODULE or use "plugincheck.settings.test" and
    # stomp on DJANGO_SETTINGS_MODULE.  This makes it easier to have
    # separate test settings.
    if 'test' in sys.argv:
        if os.environ.get('DJANGO_TEST_SETTINGS_MODULE'):
            settings_module = os.environ['DJANGO_TEST_SETTINGS_MODULE']
        else:
            settings_module = 'plugincheck.settings.test'
        os.environ['DJANGO_SETTINGS_MODULE'] = settings_module

    # If no DJANGO_SETTINGS_MODULE is specified thus far, pick an
    # appropriate one.
    if not os.environ.get('DJANGO_SETTINGS_MODULE'):
        os.environ['DJANGO_SETTINGS_MODULE'] = 'plugincheck.settings.base'

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
