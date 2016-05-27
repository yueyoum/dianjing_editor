from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.collection.models import Collection

class ResourceCollection(resources.ModelResource):
    class Meta:
        model = Collection

@admin.register(Collection)
class AdminCollection(ImportExportModelAdmin):
    resource_class = ResourceCollection
    list_display = ('id', 'talent_effect_id')