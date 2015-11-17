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
        'jingong_low', 'jingong_high',
        'qianzhi_low', 'qianzhi_high',
        'xintai_low', 'xintai_high',
        'baobing_low', 'baobing_high',
        'fangshou_low', 'fangshou_high',
        'yunying_low', 'yunying_high',
        'yishi_low', 'yishi_high',
        'caozuo_low', 'caozuo_high',
        'skill_low', 'skill_high',
    )

    fields = (
        'id',
        'league',
        ('jingong_low', 'jingong_high'),
        ('qianzhi_low', 'qianzhi_high'),
        ('xintai_low', 'xintai_high'),
        ('baobing_low', 'baobing_high'),
        ('fangshou_low', 'fangshou_high'),
        ('yunying_low', 'yunying_high'),
        ('yishi_low', 'yishi_high'),
        ('caozuo_low', 'caozuo_high'),
        ('skill_low', 'skill_high'),
    )
