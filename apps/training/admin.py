# -*- coding: utf-8 -*-

from django.contrib import admin

from apps.item.models import Item
from apps.training.models import TrainingProperty, TrainingSkill


@admin.register(TrainingProperty)
class TrainingPropertyAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'icon', 'des', 'minutes',
        'cost_type', 'cost_value', 'NeedItems', 'package', 'order_value'
    )

    def NeedItems(self, obj):
        html = []
        if obj.need_items:
            for item in obj.need_items.split(','):
                item_id, item_amount = item.split(':')
                item_name = Item.objects.get(id=int(item_id)).name

                items_text = u"{0}: {1}".format(item_name, item_amount)
                html.append(items_text)

        return u"<br />".join(html)

    NeedItems.allow_tags = True
    NeedItems.short_description = "所需物品"


@admin.register(TrainingSkill)
class TrainingSkillAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'icon', 'des', 'minutes',
    )
