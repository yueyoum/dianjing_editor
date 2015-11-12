from django.contrib import admin

from apps.ladder.models import LadderLogTemplate, LadderRankReward, LadderScoreStore

@admin.register(LadderLogTemplate)
class LadderLogTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'template')

@admin.register(LadderRankReward)
class LadderRankRewardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'package', 'reward_des',
                    'mail_title', 'mail_content'
                    )

@admin.register(LadderScoreStore)
class LadderScoreStoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'des', 'icon', 'times_limit', 'score',
                    'item', 'item_amount',
                    'training_skill', 'training_skill_amount',
                    )
