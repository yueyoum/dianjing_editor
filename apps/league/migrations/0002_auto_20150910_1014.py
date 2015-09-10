# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0006_remove_package_skill'),
        ('league', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='day_reward_lose',
            field=models.ForeignKey(related_name='league_day_reward_lose', verbose_name=b'\xe6\x97\xa5\xe5\xa5\x96\xe5\x8a\xb1\xef\xbc\x88\xe8\xbe\x93\xef\xbc\x89', blank=True, to='package.Package', null=True),
        ),
        migrations.AlterField(
            model_name='league',
            name='day_reward',
            field=models.ForeignKey(related_name='league_day_reward', verbose_name=b'\xe6\x97\xa5\xe5\xa5\x96\xe5\x8a\xb1\xef\xbc\x88\xe8\xb5\xa2\xef\xbc\x89', to='package.Package'),
        ),
    ]
