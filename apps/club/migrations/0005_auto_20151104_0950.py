# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0004_clublevel_tibu_slot_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='TibuSlot',
            fields=[
                ('id', models.IntegerField(serialize=False, verbose_name=b'\xe6\x95\xb0\xe9\x87\x8f', primary_key=True)),
                ('need_club_level', models.IntegerField(verbose_name=b'\xe6\x89\x80\xe9\x9c\x80\xe4\xbf\xb1\xe4\xb9\x90\xe9\x83\xa8\xe7\xad\x89\xe7\xba\xa7')),
                ('des', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0')),
            ],
            options={
                'db_table': 'tibu_slot',
                'verbose_name': '\u66ff\u8865\u683c\u5b50',
                'verbose_name_plural': '\u66ff\u8865\u683c\u5b50',
            },
        ),
        migrations.RemoveField(
            model_name='clublevel',
            name='tibu_slot_amount',
        ),
    ]
