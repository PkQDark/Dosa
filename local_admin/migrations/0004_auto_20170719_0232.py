# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-18 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local_admin', '0003_device_port'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='port',
            field=models.PositiveIntegerField(default=9090),
        ),
    ]