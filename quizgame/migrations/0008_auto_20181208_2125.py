# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-12-08 20:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizgame', '0007_auto_20181208_1939'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='current_question',
            new_name='current_question_nr',
        ),
    ]
