from django.contrib import admin

from apps.building.models import (
    Building,
    BuildingEffect,
    BuildingEffectInfo,
    BuildingLevels,
)


class BuildingEffectInfoInline(admin.TabularInline):
    model = BuildingEffectInfo


@admin.register(BuildingEffect)
class BuildingEffectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    inlines = [BuildingEffectInfoInline]


class BuildingLevelsInline(admin.TabularInline):
    model = BuildingLevels


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'level_up_condition_type', 'des', 'status_des',
        'day_effect', 'night_effect',
        'LevelAmount'
    )

    inlines = [BuildingLevelsInline,]

    def LevelAmount(self, obj):
        return obj.levels_info.all().count()
