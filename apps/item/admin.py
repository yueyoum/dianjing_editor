# -*- coding: utf-8 -*-

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.item.models import Item, ItemQuality


@admin.register(ItemQuality)
class ItemQualityAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'color', 'icon', 'background',
    )


class ItemResource(resources.ModelResource):
    class Meta:
        model = Item

@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin):
    resource_class = ItemResource

    list_display = (
        'id', 'tp', 'sub_tp', 'name', 'icon', 'quality',
        'des',
        'buy_type', 'buy_cost',
        'sell_gold',
        'order_value',
        'value',
    )

    list_filter = ('tp',)
    change_list_template = 'item_change_list.html'

    fieldsets = (
        (None, {
            'fields': ('id', 'tp', 'sub_tp', 'name', 'icon', 'quality',
                       'des', 'buy_type', 'buy_cost', 'sell_gold', 'order_value',
                       'value',)
        }),

        ('装备属性', {
            'classes': ('collapse',),
            'fields': ('luoji', 'minjie', 'lilun', 'wuxing', 'meili')
        })
    )
