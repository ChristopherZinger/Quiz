# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-08 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizgame', '0004_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='current_queston',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='player_answer_A',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='player_answer_B',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='player_answer_C',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='player_answer_D',
            field=models.IntegerField(default=0),
        ),
    ]