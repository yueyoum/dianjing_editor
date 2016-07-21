from django.contrib import admin

from apps.formation.models import Slot, FormationLevel, Formation

from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ResourceSlot(resources.ModelResource):
    class Meta:
        model = Slot
        bulk_replace = True

@admin.register(Slot)
class AdminSlot(ImportExportModelAdmin):
    resource_class = ResourceSlot
    list_display = ('id', 'club_level', 'des')


class ResourceFormation(resources.ModelResource):
    class Meta:
        model = Formation
        bulk_replace = True

class ResourceFormationLevel(resources.ModelResource):
    class Meta:
        model = FormationLevel
        bulk_replace = True

@admin.register(Formation)
class AdminFormation(ImportExportModelAdmin):
    resource_class = ResourceFormation
    list_display = (
        'id', 'name', 'des', 'tp',
        'active_need_star', 'active_need_items',
        'use_condition')


@admin.register(FormationLevel)
class AdminFormationLevel(ImportExportModelAdmin):
    resource_class = ResourceFormationLevel
    list_display = (
        'id', 'formation_id', 'level',
        'level_up_need_star', 'level_up_need_items',
        'talent_effects',
        'side_attack_amount'
    )