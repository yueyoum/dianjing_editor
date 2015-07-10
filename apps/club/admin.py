from django.contrib import admin

from apps.club.models import ClubFlag

@admin.register(ClubFlag)
class ClubFlagAdmin(admin.ModelAdmin):
    list_display = ('id', 'flag')
