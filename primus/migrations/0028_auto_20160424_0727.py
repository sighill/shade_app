# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-24 05:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('primus', '0027_auto_20160421_1329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='building',
            old_name='country',
            new_name='allegiance',
        ),
        migrations.RenameField(
            model_name='district',
            old_name='country',
            new_name='allegiance',
        ),
        migrations.RenameField(
            model_name='grid',
            old_name='country',
            new_name='allegiance',
        ),
        migrations.RenameField(
            model_name='island',
            old_name='country',
            new_name='allegiance',
        ),
        migrations.RenameField(
            model_name='path',
            old_name='country',
            new_name='allegiance',
        ),
        migrations.RenameField(
            model_name='town',
            old_name='country',
            new_name='allegiance',
        ),
    ]
