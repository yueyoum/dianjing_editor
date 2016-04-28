# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class NPCFormation(models.Model):
    id = models.IntegerField(primary_key=True)
    staffs = models.CharField(max_length=255, help_text='位置,选手id,兵种id;')

    class Meta:
        db_table = 'npc_formation'
        verbose_name = 'NPC阵型'
        verbose_name_plural = "NPC阵型"


    @classmethod
    def patch_fixture(cls, fixture):
        def _parse_staffs(text):
            result = []
            for x in text.split(';'):
                _a, _b, _c = x.split(',')
                result.append((int(_a), int(_b), int(_c)))

        for f in fixture:
            f['fields']['staffs'] = _parse_staffs(f['fields']['staffs'])

        return fixture