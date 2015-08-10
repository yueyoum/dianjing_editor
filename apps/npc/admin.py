from django.contrib import admin

from apps.npc.models import NPCClub, NPCClubName, NPCManagerName


@admin.register(NPCClubName)
class NPCClubNameAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(NPCManagerName)
class NPCManagerNameAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(NPCClub)
class NPCClubAdmin(admin.ModelAdmin):
    list_display = (
        'id',
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
