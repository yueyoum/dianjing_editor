from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.dungeon.models import Dungeon, DungeonGrade, DungeonResetCost



class ResourceDungeon(resources.ModelResource):
    class Meta:
        model = Dungeon
        bulk_replace = True



@admin.register(Dungeon)
class DungeonAdmin(ImportExportModelAdmin):
    resource_class = ResourceDungeon

    list_display = (
        "id", "name", "icon", "cost", "open_time", "des"
    )


class ResourceDungeonGrade(resources.ModelResource):
    class Meta:
        model = DungeonGrade
        bulk_replace = True



@admin.register(DungeonGrade)
class DungeonGradeAdmin(ImportExportModelAdmin):
    resource_class = ResourceDungeonGrade

    list_display = (
        "id", "name", "icon", "belong", "power", "need_level",
        "npc", "des"
    )


class ResourceRC(resources.ModelResource):
    class Meta:
        model = DungeonResetCost
        bulk_replace = True



@admin.register(DungeonResetCost)
class AdminBC(ImportExportModelAdmin):
    resource_class = ResourceRC
    list_display = ('id', 'dungeon_id', 'reset_times', 'diamond',)