from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.club.models import ClubFlag, ClubLevel

class ResourceClubFlag(resources.ModelResource):
    class Meta:
        model = ClubFlag
        bulk_replace = True


class ResourceClubLevel(resources.ModelResource):
    class Meta:
        model = ClubLevel
        bulk_replace = True



@admin.register(ClubFlag)
class ClubFlagAdmin(ImportExportModelAdmin):
    resource_class = ResourceClubFlag
    list_display = ('id', 'flag')

@admin.register(ClubLevel)
class ClubLevelAdmin(ImportExportModelAdmin):
    resource_class = ResourceClubLevel
    list_display = ('id', 'exp', 'energy', 'des')
