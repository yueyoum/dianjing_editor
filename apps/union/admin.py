from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.union.models import UnionLevel, UnionSignIn


class ResourceUL(resources.ModelResource):
    class Meta:
        model = UnionLevel
        bulk_replace = True

class ResourceUS(resources.ModelResource):
    class Meta:
        model = UnionSignIn
        bulk_replace = True


@admin.register(UnionLevel)
class AdminUnionLevel(ImportExportModelAdmin):
    resource_class = ResourceUL
    list_display = ('id', 'contribution', 'members_limit')

@admin.register(UnionSignIn)
class AdminUnionSignIn(ImportExportModelAdmin):
    resource_class = ResourceUS
    list_display = ('id', 'contribution', 'rewards', 'cost', 'vip')