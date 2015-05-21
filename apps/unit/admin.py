from django.contrib import admin

from apps.unit.models import Unit

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'race', 'first_trig', 'second_trig', 'third_trig',
        'skill',
        'des'
    )

    list_filter = ('race',)
