# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('division', models.CharField(max_length=200)),
                ('division_image', models.CharField(max_length=200)),
                ('conference', models.CharField(max_length=200)),
                ('league', models.CharField(max_length=200)),
                ('sport', models.CharField(max_length=200)),
                ('founded', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('number', models.IntegerField()),
                ('position', models.CharField(max_length=2)),
                ('height', models.CharField(max_length=200)),
                ('weight', models.FloatField()),
                ('age', models.FloatField()),
                ('experience', models.CharField(max_length=200)),
                ('college', models.CharField(max_length=200)),
                ('player_image', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('team', models.CharField(max_length=200)),
                ('team_image', models.CharField(max_length=400)),
                ('state', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('stadium', models.CharField(max_length=200)),
                ('stadium_image', models.DateField()),
                ('coach', models.CharField(max_length=200)),
                ('established', models.CharField(max_length=200)),
                ('conference_champs', models.CharField(max_length=200)),
                ('superbowl_champs', models.CharField(max_length=200)),
                ('division', models.ForeignKey(to='yafbdb.Division')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(to='yafbdb.Team'),
        ),
    ]
