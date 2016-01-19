# -*- coding: utf-8 -*-

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.item.models import Item, ItemQuality, Equipment


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
        'id', 'tp', 'group_id', 'name', 'icon', 'quality',
        'buy_type', 'buy_cost',
        'sell_gold',
        'order_value',
        'value',
    )

    list_filter = ('tp',)
    change_list_template = 'item_change_list.html'


class EquipmentResource(resources.ModelResource):
    class Meta:
        model = Equipment

@admin.register(Equipment)
class EquipmentAdmin(ImportExportModelAdmin):
    resource_class = EquipmentResource

    list_display = (
        'id',
        'need_club_level',
        'template_0',
        'template_1', 'template_2'
    )

    change_list_template = 'equipment_change_list.html'