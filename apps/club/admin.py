from django.contrib import admin

from apps.club.models import ClubFlag, ClubLevel

@admin.register(ClubFlag)
class ClubFlagAdmin(admin.ModelAdmin):
    list_display = ('id', 'flag')

@admin.register(ClubLevel)
class ClubLevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'exp')
