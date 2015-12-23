# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0004_policy_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='consume_per_second',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\xaf\x8f\xe7\xa7\x92\xe6\xb6\x88\xe8\x80\x97\xe8\xb5\x84\xe6\xba\x90'),
        ),
        migrations.AddField(
            model_name='unit',
            name='count_per_second',
            field=models.FloatField(default=0, verbose_name=b'\xe6\xaf\x8f\xe7\xa7\x92\xe6\x9a\xb4\xe5\x85\xb5\xe6\x95\x88\xe7\x8e\x87'),
        ),
        migrations.AddField(
            model_name='unit',
            name='draft_total_time',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x9a\xb4\xe5\x85\xb5\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AddField(
            model_name='unit',
            name='power',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x88\x98\xe6\x96\x97\xe5\x8a\x9b'),
        ),
    ]
