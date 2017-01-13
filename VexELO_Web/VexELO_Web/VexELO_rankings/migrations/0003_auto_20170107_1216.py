# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 17:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VexELO_rankings', '0002_match_match_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='event_sku',
            field=models.CharField(default='', max_length=16),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='match',
            name='event_start_date',
            field=models.DateField(default=datetime.date(1, 1, 1)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='match',
            name='match_num',
            field=models.IntegerField(),
        ),
    ]