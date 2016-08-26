# -*- coding: utf-8 -*-

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.item.models import (
    ItemQuality,
    ItemNew,
    ItemUse,
    ItemMerge,
    EquipmentBase,
    EquipmentLevel,
    ItemExp,

    EquipmentSpecial,
    EquipmentSpecialGenerate,
    EquipmentSpecialGrowingProperty,
    EquipmentSpecialLevel,
    EquipmentSpecialScoreToGrowing,
)


@admin.register(ItemQuality)
class ItemQualityAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'color', 'icon', 'background',
    )


class ResourceItemNew(resources.ModelResource):
    class Meta:
        model = ItemNew
        bulk_replace = True



class ResourceItemUse(resources.ModelResource):
    class Meta:
        model = ItemUse
        bulk_replace = True



class ResourceItemMerge(resources.ModelResource):
    class Meta:
        model = ItemMerge
        bulk_replace = True



class ResourceEquipmentBase(resources.ModelResource):
    class Meta:
        model = EquipmentBase
        bulk_replace = True



class ResourceEquipmentLevel(resources.ModelResource):
    class Meta:
        model = EquipmentLevel
        bulk_replace = True


class ResourceItemExp(resources.ModelResource):
    class Meta:
        model = ItemExp
        bulk_replace = True



@admin.register(ItemNew)
class ItemNewAdmin(ImportExportModelAdmin):
    resource_class = ResourceItemNew

    list_display = (
        'id', 'name', 'des', 'icon', 'tp', 'sub_tp', 'quality', 'stack_max'
    )

    list_filter = ('tp',)
    search_fields = ('id', 'name',)


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
        'operation', 'operation_percent',
    )

    list_filter = ('equip_id',)


@admin.register(ItemExp)
class AdminItemExp(ImportExportModelAdmin):
    resource_class = ResourceItemExp
    list_display = ('id',)



class ResourceES(resources.ModelResource):
    class Meta:
        model = EquipmentSpecial
        bulk_replace = True

@admin.register(EquipmentSpecial)
class AdminES(ImportExportModelAdmin):
    resource_class = ResourceES
    list_display = ('id', 'staff_attack', 'staff_defense', 'staff_manage', 'skills')


class ResourceESGP(resources.ModelResource):
    class Meta:
        model = EquipmentSpecialGrowingProperty
        bulk_replace = True

@admin.register(EquipmentSpecialGrowingProperty)
class AdminESGP(ImportExportModelAdmin):
    resource_class = ResourceESGP
    list_display = (
        'id',
        'growing_low', 'growing_high',
        'property_active_levels',
        'skill_active_levels',
    )

class ResourceESG(resources.ModelResource):
    class Meta:
        model = EquipmentSpecialGenerate
        bulk_replace = True

@admin.register(EquipmentSpecialGenerate)
class AdminESG(ImportExportModelAdmin):
    resource_class = ResourceESG
    list_display = (
        'id',
        'normal_cost', 'normal_generate',
        'advance_cost', 'advance_generate',
        'minutes',
    )

class ResourceESSTG(resources.ModelResource):
    class Meta:
        model = EquipmentSpecialScoreToGrowing
        bulk_replace = True

@admin.register(EquipmentSpecialScoreToGrowing)
class AdminESSTG(ImportExportModelAdmin):
    resource_class = ResourceESSTG
    list_display = ('id', 'tp', 'score_low', 'score_high', 'growing_low', 'growing_high')


class ResourceESL(resources.ModelResource):
    class Meta:
        model = EquipmentSpecialLevel
        bulk_replace = True

@admin.register(EquipmentSpecialLevel)
class AdminESL(ImportExportModelAdmin):
    resource_class = ResourceESL
    list_display = ('id', 'items')



