# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError

class AbstractTraining(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=32, verbose_name="名称")
    icon = models.CharField(max_length=32, verbose_name="图标")
    des = models.TextField(blank=True)
    minutes = models.IntegerField(verbose_name="训练所需分钟")

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True

# 属性训练
class TrainingProperty(AbstractTraining):
    TYPE = (
        (1, "属性训练"),
        (2, "经验训练"),
    )

    COST_TYPE = (
        (1, "软妹币"),
        (2, "钻石")
    )

    tp = models.IntegerField(choices=TYPE, default=1, verbose_name="类型")

    cost_type = models.IntegerField(choices=COST_TYPE, default=1, verbose_name="花费类型")
    cost_value = models.IntegerField(verbose_name="花费金额")
    need_items = models.CharField(max_length=255, verbose_name='所需物品', help_text='id:数量,id:数量')
    package = models.ForeignKey('package.Package', verbose_name="物品包")
    order_value = models.IntegerField(default=1, verbose_name='排序值')

    need_building_level = models.IntegerField(default=1, verbose_name='所需培训中心等级')

    class Meta:
        db_table = 'training_property'
        verbose_name = "属性训练"
        verbose_name_plural = "属性训练"

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            items = f['fields']['need_items']
            need_items = []
            for item in items.split(','):
                item_id, item_amount = item.split(':')
                need_items.append((int(item_id), int(item_amount)))

            f['fields']['need_items'] = need_items

        return fixture
