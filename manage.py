#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    # If no DJANGO_SETTINGS_MODULE is specified , pick an appropriate one.
    if not os.environ.get('DJANGO_SETTINGS_MODULE'):
        os.environ['DJANGO_SETTINGS_MODULE'] = 'plugincheck.settings.base'

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
