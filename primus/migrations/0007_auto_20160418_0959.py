# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-18 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primus', '0006_auto_20160418_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]