from django.contrib import admin

from apps.emoticon.models import Emoticon
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ResourceE(resources.ModelResource):
    class Meta:
        model = Emoticon
        bulk_replace = True


@admin.register(Emoticon)
class EmoticonAdmin(ImportExportModelAdmin):
    resource_class = ResourceE
    list_display = ('cmd', 'icon')
