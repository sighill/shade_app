# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-08-15 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arach', '0004_archetype_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archetype',
            name='img_id',
        ),
        migrations.AddField(
            model_name='archetype',
            name='visibility',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
