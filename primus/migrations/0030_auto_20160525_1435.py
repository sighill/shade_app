# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-25 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primus', '0029_auto_20160424_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstname',
            name='use_count',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='lastname',
            name='use_count',
            field=models.PositiveIntegerField(default=0, null=True),
        ),
    ]
