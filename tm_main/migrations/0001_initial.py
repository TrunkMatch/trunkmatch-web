# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-29 15:14
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(blank=True, max_length=40, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=40)),
                ('last_name', models.CharField(blank=True, max_length=40)),
                ('phone_number', models.CharField(blank=True, max_length=16, validators=[django.core.validators.RegexValidator(message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits.", regex=b'^\\+?1?\\d{9,15}$')])),
                ('phone_country', models.CharField(blank=True, default=b'', max_length=32, null=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('follows', models.ManyToManyField(blank=True, default=None, related_name='profile_followers', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line1', models.CharField(max_length=45, verbose_name=b'Address line 1')),
                ('address_line2', models.CharField(blank=True, max_length=45, verbose_name=b'Address line 2')),
                ('postal_code', models.CharField(max_length=10, verbose_name=b'Postal Code')),
                ('city', models.CharField(max_length=50)),
                ('state_province', models.CharField(blank=True, max_length=40, verbose_name=b'State/Province')),
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
                'ordering': ['name', 'iso_code'],
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Documentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('description', models.CharField(default=b'', max_length=512)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owning_user_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Documentation',
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
            model_name='address',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tm_main.Country'),
        ),
        migrations.AddField(
            model_name='address',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='address',
            unique_together=set([('address_line1', 'address_line2', 'postal_code', 'city', 'state_province', 'country')]),
        ),
    ]
