# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-18 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartyMessageTemplate',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('template', models.TextField()),
            ],
            options={
                'db_table': 'party_message_template',
                'verbose_name': '\u5bb4\u4f1a\u6d88\u606f\u6a21\u677f',
                'verbose_name_plural': '\u5bb4\u4f1a\u6d88\u606f\u6a21\u677f',
            },
        ),
    ]