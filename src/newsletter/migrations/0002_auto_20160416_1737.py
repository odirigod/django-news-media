# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signup',
            old_name='full_name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='signup',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
