from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.errormsg.models import ErrorMsg

class ResourceEM(resources.ModelResource):
    class Meta:
        model = ErrorMsg
        bulk_replace = True

@admin.register(ErrorMsg)
class ErrorMsgAdmin(ImportExportModelAdmin):
    resource_class = ResourceEM
    list_display = (
        'id', 'error_index', 'text_zh', 'is_retry', 'jump_to', 'des'
    )
