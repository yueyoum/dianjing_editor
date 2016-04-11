# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-11 08:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0024_auto_20160411_1618'),
        ('skill', '0014_talentskill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='category',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='race',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='type_id',
        ),
        migrations.DeleteModel(
            name='SkillAddition',
        ),
        migrations.RemoveField(
            model_name='skilllevel',
            name='skill',
        ),
        migrations.DeleteModel(
            name='SkillWashCost',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
        migrations.DeleteModel(
            name='SkillCategory',
        ),
        migrations.DeleteModel(
            name='SkillLevel',
        ),
        migrations.DeleteModel(
            name='SkillType',
        ),
    ]
