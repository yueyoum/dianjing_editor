# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
                ('advantage_add_round', models.IntegerField(verbose_name=b'\xe5\x9c\xa8\xe7\xac\xac\xe5\x87\xa0\xe8\xbd\xae\xe5\x8a\xa0\xe6\x88\x90', choices=[(1, b'\xe7\xac\xac\xe4\xb8\x80\xe8\xbd\xae'), (2, b'\xe7\xac\xac\xe4\xba\x8c\xe8\xbd\xae'), (3, b'\xe7\xac\xac\xe4\xb8\x89\xe8\xbd\xae')])),
                ('advantage_add_value', models.IntegerField(verbose_name=b'\xe5\x8a\xa0\xe6\x88\x90\xe6\x95\xb0\xe5\x80\xbc')),
                ('des', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
            ],
            options={
                'db_table': 'policy',
                'verbose_name': '\u6218\u672f',
                'verbose_name_plural': '\u6218\u672f',
            },
        ),
        migrations.CreateModel(
            name='UnitDes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('des', models.TextField(verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('policy', models.ForeignKey(to='unit.Policy')),
            ],
            options={
                'db_table': 'unit_des',
            },
        ),
        migrations.RemoveField(
            model_name='unit',
            name='des',
        ),
        migrations.AddField(
            model_name='unitdes',
            name='unit',
            field=models.ForeignKey(related_name='des', to='unit.Unit'),
        ),
    ]
