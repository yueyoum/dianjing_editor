# -*- coding: utf-8 -*-

from django.db import models

class QianBan(models.Model):
    CONDITION_TYPE = (
        (1, "装配兵种"),
    )

    id = models.IntegerField(primary_key=True)
    staff_oid = models.IntegerField()
    name = models.CharField(max_length=32, verbose_name="名字")
    des = models.TextField(verbose_name="描述")
    story_des = models.TextField(blank=True, verbose_name="背景故事")

    condition_tp = models.IntegerField(choices=CONDITION_TYPE, verbose_name="条件")
    condition_value = models.CommaSeparatedIntegerField(max_length=255, verbose_name="条件值",
                                                        help_text='id,id,id'
                                                        )

    talent_effect_id = models.IntegerField(default=0)

    class Meta:
        db_table = 'qianban'
        verbose_name = '牵绊'
        verbose_name_plural = "牵绊"


    @classmethod
    def patch_fixture(cls, fixture):
        def _parse_value(value):
            result = []
            for i in value.split(','):
                if not i:
                    continue

                result.append(int(i))

            return result

        data = {}
        for f in fixture:
            f['fields']['condition_value'] = _parse_value(f['fields']['condition_value'])
            staff_oid = f['fields'].pop('staff_oid')

            if staff_oid in data:
                data[staff_oid][f['pk']] = f['fields']
            else:
                data[staff_oid] = {f['pk']: f['fields']}

        new_fixture = []
        for k, v in data.iteritems():
            f = {
                'pk': k,
                'fields': {
                    'info': v
                }
            }

            new_fixture.append(f)

        return new_fixture
