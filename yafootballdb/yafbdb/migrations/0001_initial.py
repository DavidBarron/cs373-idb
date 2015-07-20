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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('division', models.CharField(max_length=200, default='default')),
                ('dimage', models.CharField(max_length=200, default='default')),
                ('conference', models.CharField(max_length=200, default='default')),
                ('cimage', models.CharField(max_length=200, default='default')),
                ('founded', models.CharField(max_length=200, default='default')),
                ('rchamp', models.CharField(max_length=200, default='default')),
                ('mchamps', models.CharField(max_length=200, default='default')),
                ('cnum', models.CharField(max_length=200, default='default')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200, default='default')),
                ('number', models.CharField(max_length=200, default='default')),
                ('position', models.CharField(max_length=2, default='default')),
                ('height', models.CharField(max_length=200, default='default')),
                ('weight', models.CharField(max_length=200, default='default')),
                ('age', models.CharField(max_length=200, default='default')),
                ('experience', models.CharField(max_length=200, default='default')),
                ('college', models.CharField(max_length=200, default='default')),
                ('pimage', models.CharField(max_length=400, default='default')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('team', models.CharField(max_length=200, default='default')),
                ('timage', models.CharField(max_length=400, default='default')),
                ('state', models.CharField(max_length=200, default='default')),
                ('city', models.CharField(max_length=200, default='default')),
                ('stadium', models.CharField(max_length=200, default='default')),
                ('simage', models.CharField(max_length=200, default='default')),
                ('coach', models.CharField(max_length=200, default='default')),
                ('established', models.CharField(max_length=200, default='default')),
                ('cchamps', models.CharField(max_length=200, default='default')),
                ('schamps', models.CharField(max_length=200, default='default')),
                ('twitter', models.CharField(max_length=200, default='default')),
                ('division', models.ForeignKey(to='yafbdb.Division')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(to='yafbdb.Team'),
        ),
    ]
