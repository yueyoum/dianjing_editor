# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-12 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('errormsg', '0004_errormsg_is_retry'),
    ]

    operations = [
        migrations.AddField(
            model_name='errormsg',
            name='jump_to',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]