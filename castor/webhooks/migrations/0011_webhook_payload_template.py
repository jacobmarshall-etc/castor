# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-03 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webhooks', '0010_auto_20170129_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='webhook',
            name='payload_template',
            field=models.TextField(null=True),
        ),
    ]