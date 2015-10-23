from django.contrib import admin

from apps.building.models import Building, BuildingLevels, Shop

class BuildingLevelsInline(admin.TabularInline):
    model = BuildingLevels


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'des', 'status_des', 'remark', 'LevelAmount'
    )

    inlines = [BuildingLevelsInline,]

    def LevelAmount(self, obj):
        return obj.levels_info.all().count()

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'unlock_type', 'unlock_value', 'income'
    )
