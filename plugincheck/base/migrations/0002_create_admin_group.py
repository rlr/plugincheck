# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def create_admin_group(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    admins = Group.objects.create(name='administrators')

    # Add all the permissions for all the content types of the plugins app.
    ContentType = apps.get_model('contenttypes', 'ContentType')
    contenttypes = ContentType.objects.filter(app_label='plugins')

    Permission = apps.get_model('auth', 'Permission')
    plugins_perms = Permission.objects.filter(content_type__in=contenttypes)

    for perm in plugins_perms:
        admins.permissions.add(perm)


def remove_admin_group(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(name='administrators').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_admin_group, remove_admin_group),
    ]
