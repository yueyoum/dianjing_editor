# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-11 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0030_staffequipmentleveladdition_staffequipmentqualityaddition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='quality',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='race',
        ),
        migrations.DeleteModel(
            name='StaffLevel',
        ),
        migrations.DeleteModel(
            name='StaffStatus',
        ),
        migrations.AlterField(
            model_name='staffhot',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='staffrecruitsettings',
            name='quality',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
        migrations.DeleteModel(
            name='StaffQuality',
        ),
    ]
