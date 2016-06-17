from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.skill.models import (
    Buff,
    TalentSkill,
)


class ResourceBuff(resources.ModelResource):
    class Meta:
        model = Buff
        bulk_replace = True


class ResourceTalentSkill(resources.ModelResource):
    class Meta:
        model = TalentSkill
        bulk_replace = True



@admin.register(Buff)
class AdminBuff(ImportExportModelAdmin):
    resource_class = ResourceBuff

    list_display = (
        'id', 'tp', 'level', 'effect', 'mode', 'icon'
    )


@admin.register(TalentSkill)
class AdminTalentSkill(ImportExportModelAdmin):
    resource_class = ResourceTalentSkill

    list_display = (
        'id', 'name', 'des', 'target'
    )