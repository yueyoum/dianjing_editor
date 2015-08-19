from django.contrib import admin

from apps.staff.models import (
    StaffQuality,
    StaffRace,
    StaffStatus,
    Staff,
    StaffHot,
    StaffRecruitSettings,
    StaffRecruit,
    StaffLevel,
)


@admin.register(StaffRace)
class StuffRaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(StaffQuality)
class StuffQualityAdmin(admin.ModelAdmin):
    list_display = ('id', 'color', 'icon')

@admin.register(StaffStatus)
class StuffStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value', 'des')


@admin.register(Staff)
class StuffAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'avatar', 'nation', 'race', 'quality',
        'buy_type', 'buy_cost', 'can_recruit', 'salary', 'des',
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

    inlines = [StaffRecruitSettingsInline,]

@admin.register(StaffLevel)
class StaffLevelAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'quality_A', 'quality_B', 'quality_C', 'quality_D',
        'quality_S', 'quality_SS'
    )
