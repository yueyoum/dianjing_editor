# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-09 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('union', '0002_unionexplore_unionexplorerankreward_unionmemberexplorerankreward_unionskill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unionskill',
            name='des',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='unionskill',
            name='level_up_cost',
            field=models.TextField(blank=True),
        ),
    ]
