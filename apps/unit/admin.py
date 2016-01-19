from django.contrib import admin

from apps.unit.models import Unit, Policy, UnitDes, UnitEffect

@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'icon',
        'advantage_add_round', 'advantage_add_value',
        'des'
    )


class UnitDesInline(admin.StackedInline):
    model = UnitDes


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'icon', 'name', 'race', 'tp', 'target', 'base_amount',
        'first_trig', 'second_trig', 'third_trig',
        'skill',
        'trig_at', 'trig_prob',
        'power', 'consume_per_second',
        'count_per_second',
        'draft_total_time'
    )

    list_filter = ('race',)
    inlines = [UnitDesInline,]

@admin.register(UnitEffect)
class UnitEffectAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'effect', 'race', 'tp'
    )
