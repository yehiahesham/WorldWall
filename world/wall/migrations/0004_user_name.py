# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-11 13:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0003_auto_20180311_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
