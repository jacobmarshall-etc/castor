# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webhooks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='webhook',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
