# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-29 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0022_auto_20160308_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemExp',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('exp', models.IntegerField()),
            ],
            options={
                'db_table': 'item_exp',
                'verbose_name': '\u7ecf\u9a8c\u9053\u5177',
                'verbose_name_plural': '\u7ecf\u9a8c\u9053\u5177',
            },
        ),
    ]
