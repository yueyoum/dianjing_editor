from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.package.models import Package

class PackageResource(resources.ModelResource):
    class Meta:
        model = Package

@admin.register(Package)
class PackageAdmin(ImportExportModelAdmin):
    resource_class = PackageResource

    list_display = (
        'id', 'name', 'attr_mode', 'attr_random_amount', 'attr_random_value',

        'luoji', 'minjie', 'lilun', 'wuxing', 'meili',
        'zhimingdu',

        'gold', 'diamond',
        'staff_exp', 'club_renown',

        'trainings', 'items',
        'des'
    )

    search_fields = ('name',)
