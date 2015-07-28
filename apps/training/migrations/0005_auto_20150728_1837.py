# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0005_skill_race'),
        ('training', '0004_auto_20150720_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='skill_id',
            field=models.ForeignKey(verbose_name=b'\xe6\x8a\x80\xe8\x83\xbd', blank=True, to='skill.Skill', null=True),
        ),
        migrations.AddField(
            model_name='training',
            name='skill_level',
            field=models.IntegerField(null=True, verbose_name=b'\xe6\x8a\x80\xe8\x83\xbd\xe7\xad\x89\xe7\xba\xa7', blank=True),
        ),
    ]
