# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-18 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20170407_0128'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='candonateblood',
            field=models.CharField(default='no', max_length=20),
        ),
    ]