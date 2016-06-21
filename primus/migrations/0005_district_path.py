# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-18 07:48
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('primus', '0004_auto_20160418_0947'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('gid', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('occup_cast', models.CharField(default='30,20,20,20', max_length=20)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('in_country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primus.Country')),
                ('in_region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primus.Region')),
                ('in_town', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primus.Town')),
            ],
        ),
        migrations.CreateModel(
            name='Path',
            fields=[
                ('gid', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, null=True, unique=True)),
                ('type_path', models.PositiveIntegerField(choices=[(1, 'Route'), (2, 'Rue'), (3, 'Chemin'), (4, 'Sentier'), (5, 'Pont'), (6, 'Ponton'), (7, 'Autre')])),
                ('occup_cast', models.CharField(default='30,20,20,20', max_length=20)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('geom', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
                ('in_country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primus.Country')),
                ('in_district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primus.District')),
                ('in_region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primus.Region')),
                ('in_town', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primus.Town')),
            ],
        ),
    ]
