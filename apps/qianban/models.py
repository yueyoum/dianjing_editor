# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError

class QianBan(models.Model):
    CONDITION_TYPE = (
        (1, "同时上阵"),
        (2, "装配技能"),
    )

    ADDITION = (
        ('jingong', '进攻'),
        ('qianzhi', '牵制'),
        ('xintai', '心态'),
        ('baobing', '暴兵'),
        ('fangshou', '防守'),
        ('yunying', '运营'),
        ('yishi', '意识'),
        ('caozuo', '操作'),
        ('skill', '技能强度'),
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32, unique=True, verbose_name="名字")
    des = models.TextField(verbose_name="描述")

    condition_tp = models.IntegerField(choices=CONDITION_TYPE, verbose_name="条件")
    condition_value = models.CommaSeparatedIntegerField(max_length=255, verbose_name="条件值",
                                                        help_text='id,id,id'
                                                        )

    addition_tp = models.CharField(choices=ADDITION, max_length=255, verbose_name="加成类型")
    addition_value = models.CharField(max_length=255, verbose_name="加成值",
                                                       help_text="如果加成类型是 技能强度，这里填写的是 技能id:强度"
                                                       )

    class Meta:
        db_table = 'qianban'
        verbose_name = '牵绊'
        verbose_name_plural = "牵绊"

    def clean(self):
        from apps.staff.models import Staff
        from apps.skill.models import Skill

        if self.condition_tp == 1:
            for i in self.condition_value.split(','):
                try:
                    i = int(i)
                    Staff.objects.get(id=i)
                except:
                    raise ValidationError("条件值 {0} 填错了".format(i))

        if self.condition_tp == 2:
            for i in self.condition_value.split(','):
                try:
                    i = int(i)
                    Skill.objects.get(id=i)
                except:
                    raise ValidationError("条件值 {0} 填错了".format(i))

        if self.addition_tp == 'skill':
            try:
                skills = self.addition_value.split(',')
                for s in skills:
                    a, b = s.split(':')
                    a = int(a)
                    b = int(b)
                    Skill.objects.get(id=a)
            except:
                raise ValidationError("加成值填错了")
        else:
            try:
                a = int(self.addition_value)
                assert  a > 0
            except:
                raise ValidationError("加成值填错了")


    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            condition_value = f['fields']['condition_value']
            f['fields']['condition_value'] = [int(i) for i in condition_value.split(',')]

            addition_value = f['fields'].pop('addition_value')
            f['fields']['addition_property'] = 0
            f['fields']['addition_skill'] = {}

            if f['fields']['addition_tp'] == 'skill':
                addition_skill = {}
                for s in addition_value.split(','):
                    a, b = s.split(":")
                    a = int(a)
                    b = int(b)
                    addition_skill[a] = b

                f['fields']['addition_skill'] = addition_skill
            else:
                f['fields']['addition_property'] = int(addition_value)

        return fixture
