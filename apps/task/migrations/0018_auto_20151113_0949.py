# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0017_tasktargettype_compare_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasktargettype',
            name='compare_source',
            field=models.CharField(help_text=b'\xe5\x8f\xaa\xe6\x9c\x89\xe6\xaf\x94\xe8\xbe\x83\xe7\xb1\xbb\xe5\x9e\x8b\xe6\x89\x8d\xe9\x9c\x80\xe8\xa6\x81\xe8\xae\xbe\xe7\xbd\xae', max_length=255, verbose_name=b'\xe6\xaf\x94\xe8\xbe\x83\xe6\xba\x90', blank=True),
        ),
        migrations.AlterField(
            model_name='tasktargettype',
            name='compare_type',
            field=models.IntegerField(default=1, verbose_name=b'\xe6\xaf\x94\xe8\xbe\x83\xe6\x96\xb9\xe5\xbc\x8f', choices=[(1, b'>='), (2, b'<=')]),
        ),
        migrations.AlterField(
            model_name='tasktargettype',
            name='mode',
            field=models.IntegerField(default=1, verbose_name=b'\xe5\x88\xa4\xe6\x96\xad\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(1, b'\xe6\x95\xb0\xe5\x80\xbc\xe7\xb4\xaf\xe5\x8a\xa0'), (2, b'\xe6\xaf\x94\xe8\xbe\x83')]),
        ),
    ]
