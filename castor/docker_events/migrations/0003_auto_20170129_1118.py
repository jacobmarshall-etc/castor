# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 11:18
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docker_events', '0002_auto_20170123_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dockerevent',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}, unique=True),
        ),
    ]
