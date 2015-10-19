# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0012_auto_20151016_1044'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trainingskill',
            options={'verbose_name': '\u6280\u80fd\u8bad\u7ec3\u4e66\uff08\u9053\u5177\uff09', 'verbose_name_plural': '\u6280\u80fd\u8bad\u7ec3\u4e66\uff08\u9053\u5177\uff09'},
        ),
        migrations.RemoveField(
            model_name='trainingskill',
            name='skill_id',
        ),
        migrations.RemoveField(
            model_name='trainingskill',
            name='skill_level',
        ),
    ]
