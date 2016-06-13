from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.guide.models import Guide


class ResourceGuide(resources.ModelResource):
    class Meta:
        model = Guide
        bulk_replace = True



@admin.register(Guide)
class GuideAdmin(ImportExportModelAdmin):
    resource_class = ResourceGuide

    list_display = (
        'id', 'next_id', 'operate_type', 'operate_target',
        'resume_url', 'arrow',
    )
