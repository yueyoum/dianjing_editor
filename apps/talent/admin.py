from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.talent.models import Talent

# Register your models here.


class ResourceTalent(resources.ModelResource):
    class Meta:
        model = Talent


@admin.register(Talent)
class TalentAdmin(ImportExportModelAdmin):
    resource_class = ResourceTalent

    list_display = (
            "id", "tp", "position", "name", "des",
            "image", "unlock", "up_need", "effect_id",
    )
