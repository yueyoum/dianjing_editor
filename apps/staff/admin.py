from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.staff.models import (
    StaffRace,
    StaffNew,
    StaffLevelNew,
    StaffStep,
    StaffStar,
    StaffEquipmentLevelAddition,
    StaffEquipmentQualityAddition,
    StaffRecruit,
    StaffRecruitSettings,
)


@admin.register(StaffRace)
class StuffRaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'icon', 'name')


class ResourceStaffRecruit(resources.ModelResource):
    class Meta:
        model = StaffRecruit

class ResourceStaffRecruitSettings(resources.ModelResource):
    class Meta:
        model = StaffRecruitSettings

class ResourceStaffNew(resources.ModelResource):
    class Meta:
        model = StaffNew


class ResourceStaffLevelNew(resources.ModelResource):
    class Meta:
        model = StaffLevelNew


class ResourceStaffStep(resources.ModelResource):
    class Meta:
        model = StaffStep


class ResourceStaffStar(resources.ModelResource):
    class Meta:
        model = StaffStar


class ResourceEquipQuality(resources.ModelResource):
    class Meta:
        model = StaffEquipmentQualityAddition


class ResourceEquipLevel(resources.ModelResource):
    class Meta:
        model = StaffEquipmentLevelAddition


@admin.register(StaffRecruit)
class AdminStaffRecruit(ImportExportModelAdmin):
    resource_class = ResourceStaffRecruit
    list_display = (
        'id', 'tp', 'min_point', 'items'
    )

@admin.register(StaffRecruitSettings)
class AdminStaffRecruitSettings(ImportExportModelAdmin):
    resource_class = ResourceStaffRecruitSettings
    list_display = (
        'id', 'cost_type', 'cost_value_1', 'cost_value_10',
        'items_10',
        'reward_score_times',
        'reward_score',
        'reward_score_day_limit',
        'des',
    )


@admin.register(StaffNew)
class AdminStaffNew(ImportExportModelAdmin):
    resource_class = ResourceStaffNew

    list_display = (
        'id', 'race', 'attack', 'defense', 'manage', 'operation'
    )


@admin.register(StaffLevelNew)
class AdminStaffLevelNew(ImportExportModelAdmin):
    resource_class = ResourceStaffLevelNew

    list_display = ('id', 'exp')


@admin.register(StaffStep)
class AdminStaffStep(ImportExportModelAdmin):
    resource_class = ResourceStaffStep

    list_display = ('id', 'staff_id', 'staff_step')


@admin.register(StaffStar)
class AdminStaffStar(ImportExportModelAdmin):
    resource_class = ResourceStaffStar

    list_display = ('id', 'exp', 'need_item_id', 'need_item_amount')


@admin.register(StaffEquipmentQualityAddition)
class AdminEquipQuality(ImportExportModelAdmin):
    resource_class = ResourceEquipQuality

    list_display = ('id', 'des',)


@admin.register(StaffEquipmentLevelAddition)
class AdminLevelQuality(ImportExportModelAdmin):
    resource_class = ResourceEquipLevel

    list_display = ('id', 'des',)
