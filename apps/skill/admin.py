from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.skill.models import (
    SkillType,
    SkillAddition,
    Skill,
    SkillLevel,
    SkillCategory,
    SkillWashCost,
    Buff,
    TalentSkill,
)


@admin.register(SkillType)
class SkillTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'des')

@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'des')

@admin.register(SkillAddition)
class SkillAdditionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'add_property', 'des')


class SkillLevelInLine(admin.TabularInline):
    model = SkillLevel


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'race', 'icon', 'type_id', 'category',
        'addition_ids',
        'value_base', 'level_grow',
        'des',
        'unit_des',
    )

    list_filter = ('type_id',)
    inlines = [SkillLevelInLine,]


@admin.register(SkillWashCost)
class SkillWashCostAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'cost_type', 'cost_value'
    )

class ResourceBuff(resources.ModelResource):
    class Meta:
        model = Buff

class ResourceTalentSkill(resources.ModelResource):
    class Meta:
        model = TalentSkill


@admin.register(Buff)
class AdminBuff(ImportExportModelAdmin):
    resource_class = ResourceBuff

    list_display = (
        'id', 'tp', 'level', 'effect', 'value'
    )


@admin.register(TalentSkill)
class AdminTalentSkill(ImportExportModelAdmin):
    resource_class = ResourceTalentSkill

    list_display = (
        'id', 'name', 'des', 'target'
    )