from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.match.models import (
    ChallengeMatch,
    ChallengeChapter,
    ChallengeGuide,

    Maps,
)


class ResourceChallengeChapter(resources.ModelResource):
    class Meta:
        model = ChallengeChapter


class ChallengeMatchResource(resources.ModelResource):
    class Meta:
        model = ChallengeMatch


class ResourceChallengeGuide(resources.ModelResource):
    class Meta:
        model = ChallengeGuide


@admin.register(ChallengeChapter)
class ChallengeTypeAdmin(ImportExportModelAdmin):
    resource_class = ResourceChallengeChapter
    list_display = (
        'id', 'tp', 'name', 'icon', 'des', 'star_reward', 'area'
    )


@admin.register(ChallengeMatch)
class ChallengeMatchAdmin(ImportExportModelAdmin):
    resource_class = ChallengeMatchResource

    list_display = (
        'id', 'chapter', 'name',
    )

    list_filter = ('chapter',)


@admin.register(Maps)
class MapsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'picture',
    )

@admin.register(ChallengeGuide)
class AdminChallengeGuide(ImportExportModelAdmin):
    resource_class = ResourceChallengeGuide

    list_display = (
        'id', 'guide', 'des', 'return_to_main_panel'
    )
