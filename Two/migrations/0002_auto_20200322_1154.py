# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-03-22 03:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Two', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamer',
            name='g_age',
            field=models.IntegerField(default=18, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='gamer',
            name='g_name',
            field=models.CharField(max_length=32, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='gamer',
            name='g_sex',
            field=models.NullBooleanField(default=False, verbose_name='性别'),
        ),
    ]
