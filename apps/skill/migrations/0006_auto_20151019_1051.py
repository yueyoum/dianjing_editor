# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0013_auto_20151019_1051'),
        ('skill', '0005_skill_race'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillLevel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField(verbose_name=b'\xe7\xad\x89\xe7\xba\xa7')),
                ('upgrade_training_amount', models.IntegerField(verbose_name=b'\xe5\x8d\x87\xe7\xba\xa7\xe6\x89\x80\xe9\x9c\x80\xe6\x8a\x80\xe8\x83\xbd\xe8\xae\xad\xe7\xbb\x83\xe6\x95\xb0\xe9\x87\x8f')),
            ],
            options={
                'db_table': 'skill_level',
            },
        ),
        migrations.RemoveField(
            model_name='skill',
            name='max_level',
        ),
        migrations.AddField(
            model_name='skilllevel',
            name='skill',
            field=models.ForeignKey(to='skill.Skill'),
        ),
        migrations.AddField(
            model_name='skilllevel',
            name='upgrade_training_id',
            field=models.ForeignKey(verbose_name=b'\xe5\x8d\x87\xe7\xba\xa7\xe6\x89\x80\xe9\x9c\x80\xe6\x8a\x80\xe8\x83\xbd\xe8\xae\xad\xe7\xbb\x83ID', to='training.TrainingSkill'),
        ),
    ]
