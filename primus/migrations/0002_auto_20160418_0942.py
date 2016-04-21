# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-18 07:42
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='building',
            fields=[
                ('gid', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, null=True, unique=True)),
                ('category', models.PositiveIntegerField(choices=[(1, 'Religieux'), (2, 'Militaire'), (3, 'Commercial'), (4, 'Bas-fonds'), (5, 'Privé')], null=True)),
                ('subcategory', models.PositiveIntegerField(choices=[(11, 'Cathédrale'), (12, 'Eglise'), (13, 'Chapelle'), (14, 'Temple'), (15, 'Couvent'), (16, 'Autre (religieux)'), (21, 'Caserne'), (22, 'Réserve'), (23, 'Armurerie'), (24, 'Dortoir'), (25, 'Bastion'), (26, 'Tour'), (27, 'Autre (militaire)'), (31, 'Entrepot'), (32, 'Comptoir'), (33, 'Bureau de change'), (34, 'Boutique'), (35, 'Taverne'), (36, 'Autre (commercial)'), (41, 'Planque'), (42, 'Refuge'), (43, "Lieu d'assemblée"), (44, 'Autre (bas-fonds)'), (51, 'Palazzo'), (52, 'Manoir'), (53, 'Maison bourgeoise'), (54, 'Maison modeste'), (55, 'Ruine'), (56, 'Autre (privé)')], null=True)),
                ('deity', models.PositiveIntegerField(choices=[(1, 'Thémésia'), (2, 'Ohmédia'), (3, 'Candélia'), (4, 'Sélène'), (4, 'Inconnu')], null=True)),
                ('owner', models.PositiveIntegerField(null=True)),
                ('commentary', models.CharField(max_length=1200, null=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.AlterField(
            model_name='path',
            name='type_path',
            field=models.PositiveIntegerField(choices=[(1, 'Route'), (2, 'Rue'), (3, 'Chemin'), (4, 'Sentier'), (5, 'Pont'), (6, 'Ponton'), (7, 'Autre')]),
        ),
    ]
