# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 00:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branchname', models.CharField(max_length=30, unique=True)),
                ('collegename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.College', to_field='collegename')),
                ('hostelname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Hostel', to_field='hostelname')),
                ('statename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.State', to_field='statename')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='AggregatePercentage',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentroomno',
            field=models.IntegerField(),
        ),
    ]