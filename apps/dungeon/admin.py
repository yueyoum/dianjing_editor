from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.dungeon.models import Dungeon, DungeonGrade, DungeonBuyCost



class ResourceDungeon(resources.ModelResource):
    class Meta:
        model = Dungeon


@admin.register(Dungeon)
class DungeonAdmin(ImportExportModelAdmin):
    resource_class = ResourceDungeon

    list_display = (
        "id", "name", "icon", "cost", "open_time", "des"
    )


class ResourceDungeonGrade(resources.ModelResource):
    class Meta:
        model = DungeonGrade


@admin.register(DungeonGrade)
class DungeonGradeAdmin(ImportExportModelAdmin):
    resource_class = ResourceDungeonGrade

    list_display = (
        "id", "name", "belong", "power", "need_level",
        "npc", "des"
    )


class ResourceBC(resources.ModelResource):
    class Meta:
        model = DungeonBuyCost


@admin.register(DungeonBuyCost)
class AdminBC(ImportExportModelAdmin):
    resource_class = ResourceBC
    list_display = ('id', 'diamond',)