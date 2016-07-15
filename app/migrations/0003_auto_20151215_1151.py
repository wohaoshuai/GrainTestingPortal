# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151215_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='reports',
            name='humidity',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='reports',
            name='temp',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
