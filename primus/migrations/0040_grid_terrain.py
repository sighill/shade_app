# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-01 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primus', '0039_auto_20160601_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='grid',
            name='terrain',
            field=models.PositiveIntegerField(null=True),
        ),
    ]