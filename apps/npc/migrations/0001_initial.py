# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-28 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NPCFormation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('staffs', models.CharField(help_text='\u4f4d\u7f6e,\u9009\u624bid,\u5175\u79cdid;', max_length=255)),
            ],
            options={
                'db_table': 'npc_formation',
                'verbose_name': 'NPC\u9635\u578b',
                'verbose_name_plural': 'NPC\u9635\u578b',
            },
        ),
    ]
