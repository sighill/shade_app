# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-21 06:41
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('primus', '0023_auto_20160418_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archetype',
            fields=[
                ('gid', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('cast', models.IntegerField()),
                ('category', models.IntegerField()),
                ('pui', models.IntegerField()),
                ('sou', models.IntegerField()),
                ('viv', models.IntegerField()),
                ('res', models.IntegerField()),
                ('pre', models.IntegerField()),
                ('mal', models.IntegerField()),
                ('vol', models.IntegerField()),
                ('skill', models.CharField(max_length=1200)),
                ('beauty', models.CharField(max_length=20)),
                ('heroism', models.IntegerField()),
                ('rank', models.IntegerField()),
                ('stuff', models.CharField(max_length=1200)),
                ('more', models.CharField(max_length=1200)),
            ],
        ),
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('gid', models.AutoField(db_index=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=3857)),
            ],
        ),
        migrations.DeleteModel(
            name='Grid',
        ),
        migrations.RenameField(
            model_name='district',
            old_name='in_country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='district',
            old_name='in_region',
            new_name='region',
        ),
        migrations.RenameField(
            model_name='district',
            old_name='in_town',
            new_name='town',
        ),
        migrations.RenameField(
            model_name='island',
            old_name='in_country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='island',
            old_name='in_district',
            new_name='district',
        ),
        migrations.RenameField(
            model_name='island',
            old_name='in_region',
            new_name='region',
        ),
        migrations.RenameField(
            model_name='path',
            old_name='in_country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='path',
            old_name='in_district',
            new_name='district',
        ),
        migrations.RenameField(
            model_name='path',
            old_name='in_region',
            new_name='region',
        ),
        migrations.RenameField(
            model_name='path',
            old_name='in_town',
            new_name='town',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='in_country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='town',
            old_name='in_country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='town',
            old_name='in_region',
            new_name='region',
        ),
        migrations.AddField(
            model_name='building',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primus.Country'),
        ),
        migrations.AddField(
            model_name='building',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primus.District'),
        ),
        migrations.AddField(
            model_name='building',
            name='path',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primus.Path'),
        ),
        migrations.AddField(
            model_name='building',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primus.Region'),
        ),
        migrations.AddField(
            model_name='building',
            name='town',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='primus.Town'),
        ),
        migrations.AddField(
            model_name='town',
            name='category',
            field=models.PositiveIntegerField(choices=[(1, 'Capitale'), (2, 'Cité'), (3, 'Village'), (4, 'Fort'), (5, 'Fortin')], null=True),
        ),
        migrations.AlterField(
            model_name='building',
            name='deity',
            field=models.PositiveIntegerField(choices=[(1, 'Thémésia'), (2, 'Ohmédia'), (3, 'Candélia'), (4, 'Sélène'), (5, 'Inconnu')], null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='town',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(srid=3857),
        ),
        migrations.AlterField(
            model_name='town',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
