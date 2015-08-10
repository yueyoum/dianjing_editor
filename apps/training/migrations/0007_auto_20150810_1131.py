# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0006_auto_20150728_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='building',
            field=models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe5\xbb\xba\xe7\xad\x91', blank=True, to='building.Building', null=True),
        ),
    ]
