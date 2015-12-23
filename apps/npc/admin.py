from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.npc.models import NPCClub, NPCClubName, NPCManagerName

class NPCClubNameResource(resources.ModelResource):
    class Meta:
        model = NPCClubName

class NPCManagerNameResouce(resources.ModelResource):
    class Meta:
        model = NPCManagerName

@admin.register(NPCClubName)
class NPCClubNameAdmin(ImportExportModelAdmin):
    resource_class = NPCClubNameResource
    list_display = ('name',)


@admin.register(NPCManagerName)
class NPCManagerNameAdmin(ImportExportModelAdmin):
    resource_class = NPCManagerNameResouce
    list_display = ('name',)


@admin.register(NPCClub)
class NPCClubAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'league',
        'caozuo', 'baobing', 'yunying', 'zhanshu',
        'skill_level'
    )
