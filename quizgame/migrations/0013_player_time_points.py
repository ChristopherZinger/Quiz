# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-01-04 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizgame', '0012_player_nr_of_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='time_points',
            field=models.IntegerField(default=0),
        ),
    ]
