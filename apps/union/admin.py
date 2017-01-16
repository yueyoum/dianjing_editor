from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.union.models import (
    UnionLevel,
    UnionSignIn,
    UnionExplore,
    UnionExploreRankReward,
    UnionMemberExploreRankReward,
    UnionHarassBuyTimesCost,
    UnionSkill,
)


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


class ResourceUE(resources.ModelResource):
    class Meta:
        model = UnionExplore
        bulk_replace = True

@admin.register(UnionExplore)
class AdminUE(ImportExportModelAdmin):
    resource_class = ResourceUE
    list_display = ('id', 'staffs', 'explore_reward', 'harass_reward')

class ResourceUERR(resources.ModelResource):
    class Meta:
        model = UnionExploreRankReward
        bulk_replace = True

@admin.register(UnionExploreRankReward)
class AdminUERR(ImportExportModelAdmin):
    resource_class = ResourceUERR
    list_display = ('id', 'rank_des', 'reward', 'mail_title', 'mail_content')

class ResourceUMERR(resources.ModelResource):
    class Meta:
        model = UnionMemberExploreRankReward
        bulk_replace = True

@admin.register(UnionMemberExploreRankReward)
class AdminUMERR(ImportExportModelAdmin):
    resource_class = ResourceUMERR
    list_display = ('id', 'rank_des', 'reward', 'mail_title', 'mail_content')

class ResourceUHB(resources.ModelResource):
    class Meta:
        model = UnionHarassBuyTimesCost
        bulk_replace = True

@admin.register(UnionHarassBuyTimesCost)
class AdminUHB(ImportExportModelAdmin):
    resource_class = ResourceUHB
    list_display = ('id', 'diamond')

class ResourceUSkill(resources.ModelResource):
    class Meta:
        model = UnionSkill
        bulk_replace = True

@admin.register(UnionSkill)
class AdminUSkill(ImportExportModelAdmin):
    resource_class = ResourceUSkill
    list_display = (
        'id', 'skill_id', 'level', 'name', 'icon', 'des',
        'level_up_cost', 'talent_id'
    )
