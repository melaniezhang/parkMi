# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-13 05:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20170312_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkingspot',
            name='description',
            field=models.TextField(default='YYYY-MM-DD', max_length=1000),
        ),
    ]
