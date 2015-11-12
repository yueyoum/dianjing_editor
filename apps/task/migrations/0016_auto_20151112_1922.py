# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0015_tasktargettype_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='randomevent',
            name='target',
            field=models.ForeignKey(verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b', blank=True, to='task.TaskTargetType', null=True),
        ),
        migrations.AddField(
            model_name='tasktargettype',
            name='type_category',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\xa4\xa7\xe7\xb1\xbbID'),
        ),
    ]
