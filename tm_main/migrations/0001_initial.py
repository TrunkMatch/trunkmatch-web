# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 00:04
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line1', models.CharField(max_length=45, verbose_name='Address line 1')),
                ('address_line2', models.CharField(blank=True, max_length=45, verbose_name='Address line 2')),
                ('postal_code', models.CharField(max_length=10, verbose_name='Postal Code')),
                ('city', models.CharField(max_length=50)),
                ('state_province', models.CharField(blank=True, max_length=40, verbose_name='State/Province')),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('iso_code', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name_plural': 'Countries',
                'ordering': ['name', 'iso_code'],
            },
        ),
        migrations.CreateModel(
            name='Documentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('description', models.CharField(default='', max_length=512)),
            ],
            options={
                'verbose_name_plural': 'Documentation',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=16, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits.", regex='^\\+?1?\\d{9,15}$')])),
                ('phone_country', models.CharField(blank=True, default='', max_length=32, null=True)),
                ('follows', models.ManyToManyField(related_name='profile_followers', to='tm_main.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user'],
            },
        ),
        migrations.CreateModel(
            name='StateProvince',
            fields=[
                ('iso_code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=55)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tm_main.Country')),
            ],
            options={
                'verbose_name': 'State or province',
            },
        ),
        migrations.AddField(
            model_name='documentation',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owning_user_profile', to='tm_main.Profile'),
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tm_main.Country'),
        ),
        migrations.AddField(
            model_name='address',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tm_main.Profile'),
        ),
        migrations.AlterUniqueTogether(
            name='address',
            unique_together=set([('address_line1', 'address_line2', 'postal_code', 'city', 'state_province', 'country')]),
        ),
    ]
