# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plugins', '0002_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalMime',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('name', models.CharField(max_length=255, db_index=True)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical mime',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalPlugin',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(default='', blank=True)),
                ('vendor', models.CharField(default='', max_length=255, blank=True)),
                ('url', models.URLField(default='', max_length=255, blank=True)),
                ('modified', models.DateTimeField(editable=False, blank=True)),
                ('created', models.DateTimeField(editable=False, blank=True)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical plugin',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalPluginAlias',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('plugin_id', models.IntegerField(db_index=True, null=True, blank=True)),
                ('alias', models.CharField(max_length=255)),
                ('is_regex', models.BooleanField(default=False)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical plugin alias',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HistoricalPluginRelease',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('plugin_id', models.IntegerField(db_index=True, null=True, blank=True)),
                ('os', models.CharField(default='all', max_length=32, choices=[('all', 'All'), ('win', 'Windows'), ('mac', 'Mac OS X'), ('lin', 'Linux')])),
                ('status', models.CharField(default='unknown', max_length=16, choices=[('unknown', 'unknown'), ('latest', 'latest'), ('outdated', 'outdated'), ('vulnerable', 'vulnerable'), ('should_disable', 'should_disable')])),
                ('name', models.CharField(default='', max_length=255, blank=True)),
                ('description', models.TextField(default='', blank=True)),
                ('vendor', models.CharField(default='', max_length=255, blank=True)),
                ('url', models.URLField(default='', max_length=255, blank=True)),
                ('vulnerability_description', models.TextField(default='', blank=True)),
                ('vulnerability_url', models.URLField(default='', max_length=255, blank=True)),
                ('filename', models.CharField(default='', max_length=255, blank=True)),
                ('version', models.CharField(default='', max_length=255, blank=True)),
                ('detected_version', models.CharField(default='', max_length=255, blank=True)),
                ('detection_type', models.CharField(default='*', max_length=255, blank=True)),
                ('xpi_location', models.CharField(default='', max_length=255, blank=True)),
                ('manual_installation_url', models.URLField(default='', max_length=255, blank=True)),
                ('modified', models.DateTimeField(editable=False, blank=True)),
                ('created', models.DateTimeField(editable=False, blank=True)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical plugin release',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='pluginrelease',
            name='os',
            field=models.CharField(default='all', max_length=32, choices=[('all', 'All'), ('win', 'Windows'), ('mac', 'Mac OS X'), ('lin', 'Linux')]),
            preserve_default=True,
        ),
    ]
