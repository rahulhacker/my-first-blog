# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-22 06:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='resume',
        ),
    ]
