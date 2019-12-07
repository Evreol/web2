# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-08 17:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique_for_date='posted', verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Краткое содержание')),
                ('content', models.TextField(verbose_name='Полное содержание')),
                ('posted', models.DateTimeField(db_index=True, default=datetime.datetime(2019, 10, 8, 20, 21, 52, 198808), verbose_name='Опубликована')),
                ('image', models.FileField(default='112.jpg', upload_to='', verbose_name='Путь к картинке')),
            ],
        ),
    ]
