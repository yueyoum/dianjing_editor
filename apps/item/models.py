# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError

class ItemQuality(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    color = models.CharField(max_length=32, blank=True)
    icon = models.CharField(max_length=255, blank=True)
    background = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "item_quality"
        verbose_name = "物品品质"
        verbose_name_plural = "物品品质"


class Item(models.Model):
    BUY_TYPE = (
        (0, '不可购买'),
        (1, '用 软妹币 购买'),
        (2, '用 钻石 购买'),
    )

    # type 和消息是一一对应的
    # 这里不能设置900, 因为已经在消息里被 员工卡 占用了
    ITEM_TYPE = (
        (100, '饮品'),
        (200, '徽章'),

        (300, '建筑许可证'),
        (400, '网店货物'),

        (500, '天赋石'),

        (1000, '装备'),

        (9000, '箱子'),
    )

    id = models.IntegerField(primary_key=True)
    tp = models.IntegerField(choices=ITEM_TYPE, default=1, verbose_name='类型')
    group_id = models.IntegerField(default=0, verbose_name='组ID')
    name = models.CharField(max_length=255, verbose_name='名字')
    icon = models.CharField(max_length=255, verbose_name='图标')
    quality = models.ForeignKey(ItemQuality, null=True, blank=True, verbose_name="品质")
    des = models.TextField(verbose_name='描述')

    buy_type = models.IntegerField(choices=BUY_TYPE, default=0, verbose_name='购买类型')
    buy_cost = models.IntegerField(default=0, verbose_name='购买花费')

    sell_gold = models.IntegerField(default=0, verbose_name='售卖所得软妹币', help_text='0 表示不可售卖')
    order_value = models.IntegerField(default=1, verbose_name='排序值')

    value = models.IntegerField(default=0, verbose_name='值')


    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'item'
        verbose_name = '物品'
        verbose_name_plural = '物品'

    def clean(self):
        from apps.package.models import Package

        if not self.quality:
            raise ValidationError("品质不能为空")

        if self.tp == 2000:
            if not self.value:
                raise ValidationError("箱子需要填写 物品包ID")

            if not Package.objects.filter(id=self.value).exists():
                raise ValidationError("物品包不存在")

class Equipment(models.Model):
    id = models.OneToOneField(Item, primary_key=True, db_column='id')
    need_club_level = models.IntegerField(default=0, verbose_name="使用所需俱乐部等级",
                                          help_text='0 表示没有限制'
                                          )

    luoji = models.PositiveIntegerField(default=0, verbose_name="逻辑")
    minjie = models.PositiveIntegerField(default=0, verbose_name="敏捷")
    lilun = models.PositiveIntegerField(default=0, verbose_name="理论")
    wuxing = models.PositiveIntegerField(default=0, verbose_name="悟性")
    meili = models.PositiveIntegerField(default=0, verbose_name="魅力")

    template_1 = models.CharField(max_length=255, verbose_name='属性模板1',
                                  help_text='属性:下限~上限,属性:下限~上限'
                                  )
    template_2 = models.CharField(max_length=255, verbose_name='属性模板1',
                                  help_text='属性:下限~上限,属性:下限~上限'
                                  )

    class Meta:
        db_table = 'equipment'
        verbose_name = '装备'
        verbose_name_plural = '装备'

    def clean(self):
        if self.id.tp != 1000:
            raise ValidationError("只能关联装备")

    @classmethod
    def patch_fixture(cls, fixture):
        def make_template(t):
            temp = {}
            for attr in t.split(','):
                name, value_range = attr.split(':')
                assert name in EQUIPMENT_ATTR_TEMPLATE_NAME

                low, high = value_range.split('~')
                low = int(low)
                high = int(high)

                temp[name] = (low, high)

            return temp

        for f in fixture:
            t1 = f['fields']['template_1']
            f['fields']['template_1'] = make_template(t1)

            t2 = f['fields']['template_2']
            f['fields']['template_2'] = make_template(t2)

        return fixture

# EQUIPMENT_ATTR = (
#     ('luoji', '逻辑'),
#     ('minjie', '敏捷'),
#     ('lilun', '理论'),
#     ('wuxing', '悟性'),
#     ('meili', '魅力'),
#     ('primary', '全部一级属性'),
#     ('secondary', '全部二级属性'),
# )

EQUIPMENT_ATTR_TEMPLATE_NAME = {
    'luoji', 'minjie', 'lilun', 'wuxing', 'meili',
    'primary', 'secondary',
}