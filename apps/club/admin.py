from django.contrib import admin

from apps.club.models import ClubFlag, ClubLevel, TibuSlot

@admin.register(ClubFlag)
class ClubFlagAdmin(admin.ModelAdmin):
    list_display = ('id', 'flag')

@admin.register(ClubLevel)
class ClubLevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'renown', 'max_staff_amount')

@admin.register(TibuSlot)
class TibuAdmin(admin.ModelAdmin):
    list_display = ('id', 'need_club_level', 'des')
