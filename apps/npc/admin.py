from django.contrib import admin

from apps.npc.models import NPCClub

@admin.register(NPCClub)
class NPCClubAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'manager_name',
        'jingong_low', 'jingong_high',
        'qianzhi_low', 'qianzhi_high',
        'xintai_low', 'xintai_high',
        'baobing_low', 'baobing_high',
        'fangshou_low', 'fangshou_high',
        'yunying_low', 'yunying_high',
        'yishi_low', 'yishi_high',
        'caozuo_low', 'caozuo_high',
    )

    fields = (
        'id',
        'name',
        'manager_name',
        ('jingong_low', 'jingong_high'),
        ('qianzhi_low', 'qianzhi_high'),
        ('xintai_low', 'xintai_high'),
        ('baobing_low', 'baobing_high'),
        ('fangshou_low', 'fangshou_high'),
        ('yunying_low', 'yunying_high'),
        ('yishi_low', 'yishi_high'),
        ('caozuo_low', 'caozuo_high'),
    )
