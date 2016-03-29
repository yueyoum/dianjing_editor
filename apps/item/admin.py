# -*- coding: utf-8 -*-

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.item.models import Item, ItemQuality, Equipment, ItemNew, ItemUse, ItemMerge, EquipmentBase, EquipmentLevel, ItemExp


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



class ResourceItemNew(resources.ModelResource):
    class Meta:
        model = ItemNew

class ResourceItemUse(resources.ModelResource):
    class Meta:
        model = ItemUse

class ResourceItemMerge(resources.ModelResource):
    class Meta:
        model = ItemMerge

class ResourceEquipmentBase(resources.ModelResource):
    class Meta:
        model = EquipmentBase

class ResourceEquipmentLevel(resources.ModelResource):
    class Meta:
        model = EquipmentLevel

class ResourceItemExp(resources.ModelResource):
    class Meta:
        model = ItemExp

@admin.register(ItemNew)
class ItemNewAdmin(ImportExportModelAdmin):
    resource_class = ResourceItemNew

    list_display = (
        'id', 'name', 'des', 'icon', 'tp', 'quality', 'stack_max'
    )

    list_filter = ('tp',)


@admin.register(ItemUse)
class ItemUseAdmin(ImportExportModelAdmin):
    resource_class = ResourceItemUse

    list_display = (
        'id', 'use_item_id', 'use_item_amount', 'result'
    )

@admin.register(ItemMerge)
class ItemMergeAdmin(ImportExportModelAdmin):
    resource_class = ResourceItemMerge

    list_display = (
        'id', 'amount', 'to_id', 'renown', 'crystal'
    )

@admin.register(EquipmentBase)
class EquipmentBaseAdmin(ImportExportModelAdmin):
    resource_class = ResourceEquipmentBase

    list_display = (
        'id', 'tp', 'renown'
    )

    list_filter = ('tp',)

@admin.register(EquipmentLevel)
class EquipmentLevelAdmin(ImportExportModelAdmin):
    resource_class = ResourceEquipmentLevel

    list_display = (
        'id',
        'equip_id', 'equip_level',
        'attack', 'attack_percent',
        'defense', 'defense_percent',
        'manage', 'manage_percent',
        'cost', 'cost_percent',
    )

    list_filter = ('equip_id',)

@admin.register(ItemExp)
class AdminItemExp(ImportExportModelAdmin):
    resource_class = ResourceItemExp

    list_display = ('id', 'exp')