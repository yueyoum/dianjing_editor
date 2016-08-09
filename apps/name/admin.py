from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.name.models import FirstName, LastName

class ResourceFN(resources.ModelResource):
    class Meta:
        model = FirstName
        bulk_replace = True

class ResourceLN(resources.ModelResource):
    class Meta:
        model = LastName
        bulk_replace = True

@admin.register(FirstName)
class AdminFN(ImportExportModelAdmin):
    resource_class = ResourceFN
    list_display = ('id', 'name')

@admin.register(LastName)
class AdminLN(ImportExportModelAdmin):
    resource_class = ResourceLN
    list_display = ('id', 'name')