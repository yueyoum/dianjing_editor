# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuideDialogAfter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dialog', models.TextField()),
                ('guide', models.ForeignKey(related_name='dialog_after', to='guide.Guide')),
            ],
            options={
                'db_table': 'guide_dialog_after',
                'verbose_name': '\u64cd\u4f5c\u540e\u5bf9\u8bdd',
                'verbose_name_plural': '\u64cd\u4f5c\u540e\u5bf9\u8bdd',
            },
        ),
        migrations.CreateModel(
            name='GuideDialogBefore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dialog', models.TextField()),
                ('guide', models.ForeignKey(related_name='dialog_before', to='guide.Guide')),
            ],
            options={
                'db_table': 'guide_dialog_before',
                'verbose_name': '\u64cd\u4f5c\u524d\u5bf9\u8bdd',
                'verbose_name_plural': '\u64cd\u4f5c\u524d\u5bf9\u8bdd',
            },
        ),
    ]
