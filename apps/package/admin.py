from django.contrib import admin

from apps.package.models import Package

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'attr_mode', 'attr_random_amount', 'attr_random_value',
        'jingong', 'qianzhi', 'xintai', 'baobing',
        'fangshou', 'yunying', 'yishi', 'caozuo', 'zhimingdu',
        'gold', 'diamond',
        'staff_exp', 'club_renown',
        'ladder_score', 'league_score',
        'trainings', 'items',
        'des'
    )

    search_fields = ('name',)
