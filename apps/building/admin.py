from django.contrib import admin

from apps.building.models import Building, BuildingLevels

class BuildingLevelsInline(admin.TabularInline):
    model = BuildingLevels


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'des', 'status_des', 'LevelAmount'
    )

    inlines = [BuildingLevelsInline,]

    def LevelAmount(self, obj):
        return obj.levels_info.all().count()
