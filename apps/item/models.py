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
    # 这里不能设置21, 因为已经在消息里被 员工卡 占用了
    ITEM_TYPE = (
        (1, '培训耗材'),
        (2, '网店货物'),
        (3, '建筑许可证'),
        (4, '技能训练书'),
        (11, '装备'),
        (99, '箱子'),
    )

    SUB_TYPE = (
        (0, '无子类型'),
        (1, '小型装备'),
        (2, '大型装备'),
        (3, '人物配饰'),
        (4, '信物')
    )

    id = models.IntegerField(primary_key=True)
    tp = models.IntegerField(choices=ITEM_TYPE, default=1, verbose_name='类型')
    sub_tp = models.IntegerField(choices=SUB_TYPE, default=0, verbose_name='子类型')
    name = models.CharField(max_length=255, verbose_name='名字')
    icon = models.CharField(max_length=255, verbose_name='图标')
    quality = models.ForeignKey(ItemQuality, null=True, blank=True, verbose_name="品质")
    des = models.TextField(verbose_name='描述')

    buy_type = models.IntegerField(choices=BUY_TYPE, default=0, verbose_name='购买类型')
    buy_cost = models.IntegerField(default=0, verbose_name='购买花费')

    sell_gold = models.IntegerField(default=0, verbose_name='售卖所得软妹币', help_text='0 表示不可售卖')
    order_value = models.IntegerField(default=1, verbose_name='排序值')

    value = models.IntegerField(default=0, verbose_name='值')

    # 装备用
    luoji = models.PositiveIntegerField(default=0, verbose_name="逻辑", help_text='装备需要填写')
    minjie = models.PositiveIntegerField(default=0, verbose_name="敏捷", help_text='装备需要填写')
    lilun = models.PositiveIntegerField(default=0, verbose_name="理论", help_text='装备需要填写')
    wuxing = models.PositiveIntegerField(default=0, verbose_name="悟性", help_text='装备需要填写')
    meili = models.PositiveIntegerField(default=0, verbose_name="魅力", help_text='装备需要填写')


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

        if self.tp == 11:
            if self.sub_tp == 0:
                raise ValidationError("装备不能没有子类型")

            if self.luoji == 0 and \
                self.minjie == 0 and \
                self.lilun == 0 and \
                self.wuxing == 0 and \
                self.meili == 0:
                raise ValidationError("装备属性不能全部为0")

        if self.tp == 99:
            if not self.value:
                raise ValidationError("箱子需要填写 物品包ID")

            if not Package.objects.filter(id=self.value).exists():
                raise ValidationError("物品包不存在")
