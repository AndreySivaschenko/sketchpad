# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-18 16:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sketch', '0009_auto_20170214_1710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ('notes_time',)},
        ),
    ]