# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 15:09
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('webhooks', '0001_initial'), ('webhooks', '0002_webhook_active'), ('webhooks', '0003_auto_20170123_0824'), ('webhooks', '0004_auto_20170123_0830'), ('webhooks', '0005_auto_20170123_0930'), ('webhooks', '0006_auto_20170123_0933'), ('webhooks', '0007_auto_20170123_1025'), ('webhooks', '0008_notification_status_code'), ('webhooks', '0009_auto_20170124_0057'), ('webhooks', '0010_auto_20170129_1356')]

    initial = True

    dependencies = [
        ('docker_events', '0001_initial'),
        ('docker_servers', '0003_auto_20170122_1730'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispatched_at', models.DateTimeField(auto_now=True)),
                ('delivery_duration', models.IntegerField()),
                ('request_headers', models.CharField(max_length=65535)),
                ('request_body', models.CharField(max_length=65535)),
                ('response_headers', models.CharField(max_length=65535)),
                ('response_body', models.CharField(max_length=65535)),
                ('docker_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docker_events.DockerEvent')),
            ],
        ),
        migrations.CreateModel(
            name='WebHook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payload_url', models.CharField(max_length=255)),
                ('docker_server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docker_servers.DockerServer')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='notification',
            name='webhook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webhooks.WebHook'),
        ),
        migrations.AddField(
            model_name='notification',
            name='delivered',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='failure_reason',
            field=models.TextField(blank=True, max_length=65535, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='request_body',
            field=models.CharField(max_length=65535, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='request_headers',
            field=models.CharField(max_length=65535, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='response_body',
            field=models.CharField(max_length=65535, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='response_headers',
            field=models.CharField(max_length=65535, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='request_body',
            field=models.TextField(blank=True, default='', max_length=65535),
        ),
        migrations.AlterField(
            model_name='notification',
            name='request_headers',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
        migrations.AlterField(
            model_name='notification',
            name='response_body',
            field=models.TextField(blank=True, default='', max_length=65535),
        ),
        migrations.AlterField(
            model_name='notification',
            name='response_headers',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
        migrations.AlterField(
            model_name='notification',
            name='request_body',
            field=models.TextField(blank=True, max_length=65535, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='response_body',
            field=models.TextField(blank=True, max_length=65535, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='request_headers',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}, null=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='response_headers',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='status_code',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.RenameModel(
            old_name='Notification',
            new_name='Delivery',
        ),
        migrations.AlterField(
            model_name='delivery',
            name='failure_reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='request_body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='response_body',
            field=models.TextField(blank=True, null=True),
        ),
    ]