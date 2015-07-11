# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yafbdb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='division',
            name='division_image',
        ),
        migrations.RemoveField(
            model_name='division',
            name='league',
        ),
        migrations.RemoveField(
            model_name='division',
            name='sport',
        ),
        migrations.RemoveField(
            model_name='player',
            name='player_image',
        ),
        migrations.RemoveField(
            model_name='team',
            name='conference_champs',
        ),
        migrations.RemoveField(
            model_name='team',
            name='stadium_image',
        ),
        migrations.RemoveField(
            model_name='team',
            name='superbowl_champs',
        ),
        migrations.RemoveField(
            model_name='team',
            name='team_image',
        ),
        migrations.AddField(
            model_name='division',
            name='cimage',
            field=models.CharField(max_length=200, default='default'),
        ),
        migrations.AddField(
            model_name='division',
            name='cnum',
            field=models.CharField(max_length=200, default='default'),
        ),
        migrations.AddField(
            model_name='division',
            name='dimage',
            field=models.CharField(max_length=200, default='default'),
        ),
        migrations.AddField(
            model_name='division',
            name='mchamps',
            field=models.CharField(max_length=200, default='default'),
        ),
        migrations.AddField(
            model_name='division',
            name='rchamp',
            field=models.CharField(max_length=200, default='default'),
        ),
        migrations.AddField(
            model_name='player',
            name='pimage',
            field=models.CharField(max_length=400, default='default'),
        ),
        migrations.AddField(
            model_name='team',
            name='cchamps',
            field=models.CharField(max_length=200, default='default'),
        ),
        migrations.AddField(
            model_name='team',
            name='schamps',
            field=models.CharField(max_length=200, default='default'),
        ),
        migrations.AddField(
            model_name='team',
            name='simage',
            field=models.CharField(max_length=200, default='default'),
        ),
        migrations.AddField(
            model_name='team',
            name='timage',
            field=models.CharField(max_length=400, default='default'),
        ),
        migrations.AlterField(
            model_name='division',
            name='conference',
            field=models.CharField(max_length=200, default='default'),
        ),
        migrations.AlterField(
            model_name='division',
            name='division',
            field=models.CharField(max_length=200, default='default'),
        ),
        migrations.AlterField(
            model_name='division',
            name='founded',
            field=models.CharField(max_length=200, default='default'),
        ),
        migrations.AlterField(
            model_name='player',
            name='age',
            field=models.CharField(max_length=200, default='default'),
        ),
        migrations.AlterField(
            model_name='player',
            name='college',
            field=models.CharField(max_length=200, default='default'),
        ),
        migrations.AlterField(
            model_name='player',
            name='experience',
            field=models.CharField(max_length=200, default='default'),
        ),
        migrations.AlterField(
            model_name='player',
            name='height',
            field=models.CharField(max_length=200, default='default'),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=200, default='default'),
        ),
        migrations.AlterField(
            model_name='player',
            name='number',
            field=models.CharField(max_length=200, default='default'),
        ),
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(max_length=2, default='default'),
        ),
        migrations.AlterField(
            model_name='player',
            name='weight',
            field=models.CharField(max_length=200, default='default'),
        ),
        migrations.AlterField(
            model_name='team',
            name='city',
            field=models.CharField(max_length=200, default='default'),
        ),
        migrations.AlterField(
            model_name='team',
            name='coach',
            field=models.CharField(max_length=200, default='default'),
        ),
        migrations.AlterField(
            model_name='team',
            name='established',
            field=models.CharField(max_length=200, default='default'),
        ),
        migrations.AlterField(
            model_name='team',
            name='stadium',
            field=models.CharField(max_length=200, default='default'),
        ),
        migrations.AlterField(
            model_name='team',
            name='state',
            field=models.CharField(max_length=200, default='default'),
        ),
        migrations.AlterField(
            model_name='team',
            name='team',
            field=models.CharField(max_length=200, default='default'),
        ),
    ]
