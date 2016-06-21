# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-30 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primus', '0033_auto_20160526_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('uid', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=2000)),
                ('chiffre', models.IntegerField(choices=[(1, 'Un'), (2, 'Deux'), (3, 'Trois'), (4, 'Quatre'), (5, 'Cinq'), (6, 'Six'), (7, 'Sept'), (8, 'Huit'), (9, 'Neuf')])),
            ],
        ),
    ]
