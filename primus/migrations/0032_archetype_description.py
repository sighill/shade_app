# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-26 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primus', '0031_auto_20160526_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='archetype',
            name='description',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
