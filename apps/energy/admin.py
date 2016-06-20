from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.energy.models import BuyCost

class ResourceBuyCost(resources.ModelResource):
    class Meta:
        model = BuyCost
        bulk_replace = True


class AdminBuyCost(ImportExportModelAdmin):
    resource_class = ResourceBuyCost
    list_display = ('id', 'cost',)
