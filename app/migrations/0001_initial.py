# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-15 17:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptype', models.CharField(max_length=50)),
                ('min_price', models.FloatField(default=0)),
                ('max_price', models.FloatField(default=0)),
                ('date', models.DateField()),
                ('available', models.DateField()),
                ('quantity', models.FloatField(default=0)),
                ('id1', models.CharField(default=0, max_length=3)),
                ('temp', models.CharField(default=0, max_length=50)),
                ('humidity', models.CharField(default=0, max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_mod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zipcode', models.FloatField(default=0)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]