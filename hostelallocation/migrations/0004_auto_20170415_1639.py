# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-15 16:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostelallocation', '0003_auto_20170406_0049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostelallocation',
            name='studentrollno',
        ),
        migrations.DeleteModel(
            name='HostelAllocation',
        ),
    ]
