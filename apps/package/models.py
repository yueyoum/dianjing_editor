# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError


class Package(models.Model):
    ATTR_MODE = (
        (1, "不加成属性"),
        (2, "完全随机"),
        (3, "从设定的属性中随机"),
        (4, "设定的属性")
    )

    ATTRS = {
        'attr_random_value': "随机熟悉值范围",
        'jingong': "进攻",
        'qianzhi': "牵制",
        'xintai': "心态",
        'baobing': "暴兵",
        'fangshou': "防守",
        'yunying': "运营",
        'yishi': "意识",
        'caozuo': "操作",
        'gold': "软妹币",
        'diamond': "钻石",
        'staff_exp': "员工经验",
        'club_renown': "俱乐部声望"
    }


    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32, verbose_name="名字")

    attr_mode = models.IntegerField(choices=ATTR_MODE, default=1, verbose_name="属性模式")
    attr_random_amount = models.IntegerField(default=1, verbose_name="随机属性数量",
                                             help_text="只有 属性模式 为 随机 时，才有用"
                                             )
    attr_random_value = models.CharField(blank=True, max_length=32, verbose_name="随机属性值范围",
                                         help_text="只有 属性模式 为 完全随机 时，才有用"
                                         )


    jingong = models.CharField(max_length=32, blank=True, verbose_name="进攻")
    qianzhi = models.CharField(max_length=32, blank=True, verbose_name="牵制")
    xintai = models.CharField(max_length=32, blank=True, verbose_name="心态")
    baobing = models.CharField(max_length=32, blank=True, verbose_name="暴兵")
    fangshou = models.CharField(max_length=32, blank=True, verbose_name="防守")
    yunying = models.CharField(max_length=32, blank=True, verbose_name="运营")
    yishi = models.CharField(max_length=32, blank=True, verbose_name="意识")
    caozuo = models.CharField(max_length=32, blank=True, verbose_name="操作")

    gold = models.CharField(max_length=32, blank=True, verbose_name="软妹币")
    diamond = models.CharField(max_length=32, blank=True, verbose_name="钻石")

    staff_exp = models.CharField(max_length=32, blank=True, verbose_name="员工经验")
    club_renown = models.CharField(max_length=32, blank=True, verbose_name="俱乐部声望")

    des = models.TextField(blank=True, verbose_name="描述")


    def __unicode__(self):
        return self.name


    def clean(self):
        for attr, name in self.ATTRS.iteritems():
            value = getattr(self, attr)
            if not value:
                continue

            if ',' not in value:
                if not value.isdigit():
                    raise ValidationError("{0}填错了".format(name))
            else:
                value_splited = value.split(',')
                if len(value_splited) != 2:
                    raise ValidationError("{0}填错了".format(name))

                for v in value_splited:
                    if not v.isdigit():
                        raise ValidationError("{0}填错了".format(name))


    class Meta:
        db_table = 'package'
        verbose_name = "物品包"
        verbose_name_plural = "物品包"


    @classmethod
    def patch_fixture(cls, fixture):
        def patch(value):
            if ',' in value:
                a, b = value.split(',')
                return [int(a), int(b)]

            return [int(value), int(value)]

        for f in fixture:
            for k in cls.ATTRS.keys():
                f['fields'][k] = patch(f['fields'][k])

        return fixture

