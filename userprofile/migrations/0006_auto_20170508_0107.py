# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-07 22:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_auto_20170403_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.URLField(verbose_name='Фоток'),
        ),
    ]