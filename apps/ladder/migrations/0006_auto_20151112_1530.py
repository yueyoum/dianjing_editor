# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0015_trainingproperty_need_building_level'),
        ('item', '0003_item_order_value'),
        ('ladder', '0005_remove_ladderrankreward_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ladderscorestore',
            name='package',
        ),
        migrations.AddField(
            model_name='ladderscorestore',
            name='item',
            field=models.ForeignKey(verbose_name=b'\xe7\x89\xa9\xe5\x93\x81', blank=True, to='item.Item', null=True),
        ),
        migrations.AddField(
            model_name='ladderscorestore',
            name='item_amount',
            field=models.IntegerField(null=True, verbose_name=b'\xe7\x89\xa9\xe5\x93\x81\xe6\x95\xb0\xe9\x87\x8f', blank=True),
        ),
        migrations.AddField(
            model_name='ladderscorestore',
            name='training_skill',
            field=models.ForeignKey(verbose_name=b'\xe6\x8a\x80\xe8\x83\xbd\xe8\xae\xad\xe7\xbb\x83\xe4\xb9\xa6', blank=True, to='training.TrainingSkill', null=True),
        ),
        migrations.AddField(
            model_name='ladderscorestore',
            name='training_skill_amount',
            field=models.IntegerField(null=True, verbose_name=b'\xe6\x8a\x80\xe8\x83\xbd\xe8\xae\xad\xe7\xbb\x83\xe4\xb9\xa6\xe6\x95\xb0\xe9\x87\x8f', blank=True),
        ),
    ]
