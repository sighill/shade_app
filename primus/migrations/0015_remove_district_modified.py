# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-18 11:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('primus', '0014_auto_20160418_1233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='district',
            name='modified',
        ),
    ]
