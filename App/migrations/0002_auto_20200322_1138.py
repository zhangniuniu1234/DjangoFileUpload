# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-03-22 03:38
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_title', models.CharField(max_length=12)),
                ('b_content', tinymce.models.HTMLField()),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='s_pic',
            field=models.ImageField(upload_to='s_icons/%Y/%m/%d'),
        ),
    ]
