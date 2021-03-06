from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.unit.models import UnitNew, UnitLevel, UnitStep, UnitLevelAddition, UnitStepAddition, UnitUnLock

class ResourceUnitNew(resources.ModelResource):
    class Meta:
        model = UnitNew
        bulk_replace = True


class ResourceUnitUnLock(resources.ModelResource):
    class Meta:
        model = UnitUnLock
        bulk_replace = True


class ResourceUnitLevel(resources.ModelResource):
    class Meta:
        model = UnitLevel
        bulk_replace = True


class ResourceUnitStep(resources.ModelResource):
    class Meta:
        model = UnitStep
        bulk_replace = True


class ResourceUnitLevelAddition(resources.ModelResource):
    class Meta:
        model = UnitLevelAddition
        bulk_replace = True


class ResourceUnitStepAddition(resources.ModelResource):
    class Meta:
        model = UnitStepAddition
        bulk_replace = True


@admin.register(UnitNew)
class AdminUnitNew(ImportExportModelAdmin):
    resource_class = ResourceUnitNew

    list_display = (
        'id', 'name', 'model', 'scale', 'icon', 'tp', 'race',
    )

@admin.register(UnitUnLock)
class AdminUnitUnLock(ImportExportModelAdmin):
    resource_class = ResourceUnitUnLock

    list_display = (
        'id', 'need_club_level', 'need_unit_level'
    )


@admin.register(UnitLevel)
class AdminUnitLevel(ImportExportModelAdmin):
    resource_class = ResourceUnitLevel

    list_display = (
        'id', 'unit_id', 'unit_level', 'update_item_need',
        'hp', 'attack', 'defense'
    )

@admin.register(UnitStep)
class AdminUnitStep(ImportExportModelAdmin):
    resource_class = ResourceUnitStep

    list_display = (
        'id', 'unit_id', 'unit_step', 'level_limit', 'update_item_need'
    )

@admin.register(UnitLevelAddition)
class AdminUnitLevelAddition(ImportExportModelAdmin):
    resource_class = ResourceUnitLevelAddition

    list_display = (
        'id', 'race', 'level'
    )


@admin.register(UnitStepAddition)
class AdminUnitStepAddition(ImportExportModelAdmin):
    resource_class = ResourceUnitStepAddition

    list_display = (
        'id', 'race', 'step'
    )
