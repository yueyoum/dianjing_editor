from django.contrib import admin

from apps.skill.models import (
    SkillType,
    SkillAddition,
    Skill
)


@admin.register(SkillType)
class SkillTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'des')


@admin.register(SkillAddition)
class SkillAdditionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'add_property', 'des')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'race', 'icon', 'type_id', 'addition_ids',
        'value_base', 'level_grow', 
        'des',
    )

    list_filter = ('type_id',)
