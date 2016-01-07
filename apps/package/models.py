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
        'attr_random_value': "随机属性值范围",

        'caozuo': "操作",
        'baobing': "暴兵",
        'jingying': "经营",
        'zhanshu': "战术",

        'biaoyan': "表演",
        'yingxiao': "营销",

        'zhimingdu': "知名度",

        'gold': "软妹币",
        'diamond': "钻石",
        'staff_exp': "员工经验",
        'club_renown': "俱乐部声望",
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

    caozuo = models.CharField(max_length=32, blank=True, verbose_name="操作")
    baobing = models.CharField(max_length=32, blank=True, verbose_name="暴兵")
    jingying = models.CharField(max_length=32, blank=True, verbose_name="经营")
    zhanshu = models.CharField(max_length=32, blank=True, verbose_name="战术")

    biaoyan = models.CharField(max_length=32, blank=True, verbose_name="表演")
    yingxiao = models.CharField(max_length=32, blank=True, verbose_name="营销")

    zhimingdu = models.CharField(max_length=32, blank=True, verbose_name="知名度")

    gold = models.CharField(max_length=32, blank=True, verbose_name="软妹币")
    diamond = models.CharField(max_length=32, blank=True, verbose_name="钻石")

    staff_exp = models.CharField(max_length=32, blank=True, verbose_name="员工经验")
    club_renown = models.CharField(max_length=32, blank=True, verbose_name="俱乐部声望")

    items = models.CharField(max_length=255, blank=True, verbose_name="物品",
                             help_text="id:数量,id:数量"
                             )

    staffs = models.CommaSeparatedIntegerField(max_length=255, blank=True, verbose_name="员工",
                              help_text="id,id,id"
                              )

    staff_cards = models.CharField(max_length=255, blank=True, verbose_name="员工卡",
                                   help_text='id:数量,id:数量'
                                   )

    des = models.TextField(blank=True, verbose_name="描述")

    def __unicode__(self):
        return self.name

    def clean(self):
        from apps.item.models import Item
        from apps.staff.models import Staff

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

                if int(value_splited[0]) > int(value_splited[1]):
                    raise ValidationError("{0}填错了".format(name))

        if self.items:
            items = self.items.split(',')
            for i in items:
                try:
                    _id, amount = i.split(':')
                    _id = int(_id)
                    amount = int(amount)
                except:
                    raise ValidationError("物品填错了")

                if not Item.objects.filter(id=int(_id)).exists():
                    raise ValidationError("物品{0}不存在".format(_id))

        if self.staffs:
            staffs = self.staffs.split(',')
            for i in staffs:
                if not i.isdigit():
                    raise ValidationError("员工ID填错了")

                if not Staff.objects.filter(id=int(i)).exists():
                    raise ValidationError("员工{0}不存在".format(i))

        if self.staff_cards:
            staff_cards = self.staff_cards.split(',')
            for i in staff_cards:
                try:
                    _id, amount = i.split(':')
                    _id = int(_id)
                    amount = int(amount)
                except:
                    raise ValidationError("员工卡填错了")

                if not Staff.objects.filter(id=_id).exists():
                    raise ValidationError("员工{0}不存在".format(_id))


    class Meta:
        db_table = 'package'
        verbose_name = "物品包"
        verbose_name_plural = "物品包"

    @classmethod
    def patch_fixture(cls, fixture):
        def patch(value):
            if not value:
                return []

            if ',' in value:
                a, b = value.split(',')
                return [int(a), int(b)]

            return [int(value), int(value)]

        for f in fixture:
            for k in cls.ATTRS.keys():
                f['fields'][k] = patch(f['fields'][k])

            items = f['fields']['items']
            new_items = []
            if items:
                for i in items.split(','):
                    _id, amount = i.split(':')
                    new_items.append((int(_id), int(amount)))

            f['fields']['items'] = new_items

            if f['fields']['staffs']:
                staffs = [int(i) for i in f['fields']['staffs'].split(',')]
            else:
                staffs = []
            f['fields']['staffs'] = staffs

            staff_cards = f['fields']['staff_cards']
            new_staff_cards = []
            if staff_cards:
                for i in staff_cards.split(','):
                    _id, amount = i.split(':')
                    new_staff_cards.append((int(_id), int(amount)))

            f['fields']['staff_cards'] = new_staff_cards

        return fixture