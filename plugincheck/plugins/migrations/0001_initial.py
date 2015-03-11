# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Plugin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(default='', blank=True)),
                ('vendor', models.CharField(default='', max_length=255, blank=True)),
                ('url', models.URLField(default='', max_length=255, blank=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('mimes', models.ManyToManyField(to='plugins.Mime', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PluginAlias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alias', models.CharField(max_length=255)),
                ('is_regex', models.BooleanField(default=False)),
                ('plugin', models.ForeignKey(to='plugins.Plugin')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PluginRelease',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('os', models.CharField(default='*', max_length=32, choices=[('*', 'All'), ('win', 'Windows'), ('mac', 'Mac OS X'), ('lin', 'Linux')])),
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
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('plugin', models.ForeignKey(to='plugins.Plugin')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='pluginrelease',
            unique_together=set([('plugin', 'os', 'version', 'detected_version', 'detection_type')]),
        ),
        migrations.AlterUniqueTogether(
            name='pluginalias',
            unique_together=set([('plugin', 'alias', 'is_regex')]),
        ),
    ]
