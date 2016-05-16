from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.territory.models import (
    TerritoryBuilding,
    BuildingSlot,
    BuildingSlotExtraProduct,
    StaffSpecialProduct,
    Inspire,
)

class ResourceTerritoryBuilding(resources.ModelResource):
    class Meta:
        model = TerritoryBuilding

class ResourceBuildingSlot(resources.ModelResource):
    class Meta:
        model = BuildingSlot

class ResourceBuildingSlotExtraProduct(resources.ModelResource):
    class Meta:
        model = BuildingSlotExtraProduct

class ResourceStaffSpecialProduct(resources.ModelResource):
    class Meta:
        model = StaffSpecialProduct

class ResourceInspire(resources.ModelResource):
    class Meta:
        model = Inspire



@admin.register(TerritoryBuilding)
class AdminTerritoryBuilding(ImportExportModelAdmin):
    resource_class = ResourceTerritoryBuilding
    list_display = (
        'id', 'building_id', 'building_name', 'building_level',
        'exp', 'product_rate', 'events', 'product_limit'
    )

    list_filter = ('building_id',)

@admin.register(BuildingSlot)
class AdminBuildingSlot(ImportExportModelAdmin):
    resource_class = ResourceBuildingSlot
    list_display = (
        'id', 'building_id', 'need_building_level', 'need_vip_level',
        'exp_modulus'
    )

    list_filter = ('building_id',)

@admin.register(BuildingSlotExtraProduct)
class AdminBuildingSlotExtraProduct(ImportExportModelAdmin):
    resource_class = ResourceBuildingSlotExtraProduct
    list_display = (
        'id', 'slot_id', 'building_level', 'extra_product', 'cost_amount'
    )

    list_filter = ('slot_id',)

@admin.register(StaffSpecialProduct)
class AdminStaffSpecialProduct(ImportExportModelAdmin):
    resource_class = ResourceStaffSpecialProduct
    list_display = (
        'id', 'product_1', 'product_2', 'product_3'
    )

@admin.register(Inspire)
class AdminInspire(ImportExportModelAdmin):
    resource_class = ResourceInspire
    list_display = (
        'id', 'building_id', 'building_level', 'exp', 'max_times', 'reward'
    )