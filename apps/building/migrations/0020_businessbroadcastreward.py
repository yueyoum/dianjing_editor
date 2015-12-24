# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_item_order_value'),
        ('building', '0019_buildinglevels_effect_des'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessBroadcastReward',
            fields=[
                ('id', models.OneToOneField(primary_key=True, serialize=False, to='item.Item', verbose_name=b'\xe7\x89\xa9\xe5\x93\x81')),
                ('amount', models.IntegerField(verbose_name=b'\xe6\x95\xb0\xe9\x87\x8f')),
            ],
            options={
                'db_table': 'business_broadcast_reward',
                'verbose_name': '\u76f4\u64ad\u83b7\u5f97\u7269\u54c1',
                'verbose_name_plural': '\u76f4\u64ad\u83b7\u5f97\u7269\u54c1',
            },
        ),
    ]
