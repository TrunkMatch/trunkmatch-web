# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 03:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tm_main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='follows',
            field=models.ManyToManyField(blank=True, related_name='profile_followers', to='tm_main.Profile'),
        ),
    ]
