from django.contrib import admin

from apps.league.models import League

@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'daily_reward', 'up_need_score', 'des', 'icon_path'
    )
