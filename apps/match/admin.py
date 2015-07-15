from django.contrib import admin

from apps.match.models import ChallengeType, ChallengeMatch

@admin.register(ChallengeType)
class ChallengeTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'level', 'des'
    )


@admin.register(ChallengeMatch)
class ChallengeMatchAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'next_id', 'name', 'tp', 'level', 'strength', 'staffs'
    )

    list_filter = ('tp',)
