# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-11-30 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('question', models.CharField(max_length=1000)),
                ('answer_A', models.CharField(max_length=100)),
                ('answer_B', models.CharField(max_length=100)),
                ('answer_C', models.CharField(max_length=100)),
                ('answer_D', models.CharField(max_length=100)),
                ('answer_A_img', models.ImageField(blank=True, null=True, upload_to='question/')),
                ('answer_B_img', models.ImageField(blank=True, null=True, upload_to='question/')),
                ('answer_C_img', models.ImageField(blank=True, null=True, upload_to='question/')),
                ('answer_D_img', models.ImageField(blank=True, null=True, upload_to='question/')),
            ],
        ),
    ]