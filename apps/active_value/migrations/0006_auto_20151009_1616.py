# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('active_value', '0005_activefunction_des'),
    ]

    operations = [
        migrations.AddField(
            model_name='activereward',
            name='value',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\xb4\xbb\xe8\xb7\x83\xe5\xba\xa6'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activereward',
            name='id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
