# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-08 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
