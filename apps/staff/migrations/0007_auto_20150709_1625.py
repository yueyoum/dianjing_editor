# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0006_remove_staffrecruit_recruit_settings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffrecruitsettings',
            name='recruit',
            field=models.ForeignKey(related_name='statff_settings', to='staff.StaffRecruit'),
        ),
    ]
