# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-05 17:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('local_admin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='slug',
        ),
    ]