from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.staff.models import (
    StaffQuality,
    StaffRace,
    StaffStatus,
    Staff,
    StaffHot,
    StaffRecruitSettings,
    StaffRecruit,
    StaffLevel,
    StaffNew,
    StaffLevelNew,
    StaffStep,
    StaffStar,
)


class StaffResource(resources.ModelResource):
    class Meta:
        model = Staff


@admin.register(StaffRace)
class StuffRaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'icon', 'name')


@admin.register(StaffQuality)
class StuffQualityAdmin(admin.ModelAdmin):
    list_display = ('id', 'color', 'icon', 'background', 'background_half')


@admin.register(StaffStatus)
class StuffStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'icon', 'name', 'value', 'des')


@admin.register(Staff)
class StuffAdmin(ImportExportModelAdmin):
    resource_class = StaffResource

    list_display = (
        'id', 'name', 'avatar', 'picture', 'nation', 'gender', 'race', 'quality',
        'buy_type', 'buy_cost', 'can_recruit', 'salary',
        'skill_ids', 'qianban_ids'
    )

    list_filter = ('race', 'quality')


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


@admin.register(StaffLevel)
class StaffLevelAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'quality_C', 'quality_B', 'quality_A',
        'quality_S', 'quality_SS'
    )

    fields = (
        'id',
        'quality_C',
        'quality_B',
        'quality_A',
        'quality_S',
        'quality_SS',
    )

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


@admin.register(StaffNew)
class AdminStaffNew(ImportExportModelAdmin):
    resource_class = ResourceStaffNew

    list_display = (
        'id', 'name', 'picture', 'race', 'attack', 'defense', 'manage', 'operation'
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
