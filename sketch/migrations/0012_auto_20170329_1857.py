# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-29 15:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sketch', '0011_profiles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profiles',
        ),
    ]
