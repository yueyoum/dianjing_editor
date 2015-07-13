from django.contrib import admin

from apps.unit.models import Unit, Policy, UnitDes

@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name',
        'advantage_add_round', 'advantage_add_value',
        'des'
    )


class UnitDesInline(admin.StackedInline):
    model = UnitDes


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'race', 'first_trig', 'second_trig', 'third_trig',
        'skill',
        'des'
    )

    list_filter = ('race',)
    inlines = [UnitDesInline,]
