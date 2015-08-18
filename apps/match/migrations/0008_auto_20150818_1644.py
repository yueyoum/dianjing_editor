# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0007_challengematch_package'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchconversationend',
            name='disadvantage_value',
            field=models.IntegerField(blank=True, null=True, verbose_name=b'\xe5\x8a\xa3\xe5\x8a\xbf\xe6\x96\xb9\xe4\xbc\x98\xe5\x8a\xbf\xe5\x80\xbc', choices=[(50, b'=50'), (49, b'40<=, <50'), (39, b'30<=, <40'), (29, b'20<=, <30'), (19, b'10<=, <20'), (9, b'0<=, <10'), (0, b'\xe6\x97\xa0\xe5\x85\xb3\xe7\xb4\xa7\xe8\xa6\x81')]),
        ),
    ]
