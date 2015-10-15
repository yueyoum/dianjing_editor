# -*- coding: utf-8 -*-

from django.contrib import admin

from apps.item.models import Item
from apps.training.models import TrainingType, Training, TrainingProperty, TrainingSkill

@admin.register(TrainingType)
class TrainingTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'on_sell', 'tp', 'icon', 'des',
        'cost_type', 'cost_value', 'need_building_level',
        'minutes', 'package',
        'skill_id', 'skill_level',
    )


@admin.register(TrainingProperty)
class TrainingPropertyAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'icon', 'des', 'minutes',
        'cost_type', 'cost_value', 'NeedItems', 'package', 'order_value'
    )

    def NeedItems(self, obj):
        html = []
        for item in obj.need_items.split(','):
            item_id, item_amount = item.split(':')
            item_name = Item.objects.get(id=int(item_id)).name

            items_text = "{0}: {1}".format(item_name, item_amount)
            html.append(items_text)

        return u"<br />".join(html)

    NeedItems.allow_tags = True
    NeedItems.short_description = "所需物品"


@admin.register(TrainingSkill)
class TrainingSkillAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'icon', 'des', 'minutes',
        'skill_id', 'skill_level'
    )
