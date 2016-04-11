from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.staff.models import (
    StaffRace,
    StaffHot,
    StaffRecruitSettings,
    StaffRecruit,
    StaffNew,
    StaffLevelNew,
    StaffStep,
    StaffStar,
    StaffEquipmentLevelAddition,
    StaffEquipmentQualityAddition,
)


@admin.register(StaffRace)
class StuffRaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'icon', 'name')


@admin.register(StaffHot)
class StaffHotAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'cost'
    )


class StaffRecruitSettingsInline(admin.TabularInline):
    model = StaffRecruitSettings


@admin.register(StaffRecruit)
class StaffRecruitAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'cost_type', 'cost_value', 'lucky_times',
        'des'
    )

    inlines = [StaffRecruitSettingsInline, ]


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
