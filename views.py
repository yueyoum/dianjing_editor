# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       views
Date Created:   2015-04-23 16:42
Description:

"""
import datetime

from cStringIO import StringIO
import zipfile

from django.http import HttpResponse

from misc import get_fixture

MODELS = (
    ('config.ClientConfig', 'client_config.json'),
    ('config.GlobalConfig', 'global_config.json'),
    ('ui.UI', 'ui.json'),
    ('ui.BackgroundImage', 'background_image.json'),

    ('errormsg.ErrorMsg', 'errormsg.json'),

    ('staff.StaffRace', 'staff_race.json'),
    ('staff.StaffRecruit', 'staff_recruit.json'),
    ('staff.StaffNew', 'staff_new.json'),
    ('staff.StaffLevelNew', 'staff_level_new.json'),
    ('staff.StaffStar', 'staff_star.json'),
    ('staff.StaffEquipmentQualityAddition', 'staff_equip_quality_addition.json'),
    ('staff.StaffEquipmentLevelAddition', 'staff_equip_level_addition.json'),

    ('unit.UnitNew', 'unit_new.json'),
    ('unit.UnitLevelAddition', 'unit_level_addition.json'),
    ('unit.UnitStepAddition', 'unit_step_addition.json'),
    ('unit.UnitUnLock', 'unit_unlock.json'),

    ('skill.Buff', 'skill_buff.json'),
    ('skill.TalentSkill', 'talent_skill.json'),
    ('club.ClubFlag', 'club_flag.json'),
    ('club.ClubLevel', 'club_level.json'),

    ('qianban.QianBan', 'qianban.json'),
    ('qianban.Inspire', 'inspire.json'),
    ('qianban.InspireLevelAddition', 'inspire_level_addition.json'),
    ('qianban.InspireStepAddition', 'inspire_step_addition.json'),

    ('match.ChallengeArea', 'challenge_area.json'),
    ('match.ChallengeChapter', 'challenge_chapter.json'),
    ('match.ChallengeMatch', 'challenge_match.json'),
    ('match.ChallengeGuide', 'challenge_guide.json'),
    ('match.ChallengeBuyCost', 'challenge_buy_cost.json'),

    ('building.BuildingNew', 'building.json'),

    ('task.TaskCondition', 'task_condition.json'),
    ('task.TaskMain', 'task_main.json'),
    ('task.TaskDaily', 'task_daily.json'),


    ('notification.Notification', 'notification.json'),

    ('function.Function', 'function.json'),
    ('function.FunctionTips', 'function_tips.json'),

    ('resources.Resource', 'resource.json'),

    ('emoticon.Emoticon', 'emoticon.json'),
    ('guide.Guide', 'guide.json'),

    ('template.BroadcastTemplate', 'broadcast_template.json'),

    ('conversation.ChallengeConversation', 'challenge_conversation.json'),

    ('item.ItemQuality', 'item_quality.json'),
    ('item.ItemNew', 'item_new.json'),
    ('item.ItemUse', 'item_use.json'),
    ('item.ItemMerge', 'item_merge.json'),
    ('item.EquipmentBase', 'equipment_new.json'),
    ('item.ItemExp', 'item_exp.json'),

    ('item.EquipmentSpecial', 'equipment_special.json'),
    ('item.EquipmentSpecialGrowingProperty', 'equipment_special_growing_property.json'),
    ('item.EquipmentSpecialGenerate', 'equipment_special_generate.json'),
    ('item.EquipmentSpecialScoreToGrowing', 'equipment_special_score_to_growing.json'),
    ('item.EquipmentSpecialLevel', 'equipment_special_level.json'),

    ('talent.Talent', 'talent.json'),
    ('vip.VIP', 'vip.json'),

    ('dungeon.Dungeon', 'dungeon.json'),
    ('dungeon.DungeonGrade', 'dungeon_grade.json'),
    ('dungeon.DungeonResetCost', 'dungeon_reset_cost.json'),

    ('npc.NPCFormation', 'npc_formation.json'),

    ('arena.ArenaNPC', 'arena_npc.json'),
    ('arena.HonorReward', 'arena_honor_reward.json'),
    ('arena.RankReward', 'arena_rank_reward.json'),
    ('arena.RankRewardWeekly', 'arena_rank_reward_weekly.json'),
    ('arena.MatchReward', 'arena_match_reward.json'),
    ('arena.BuyTimesCost', 'arena_buy_times_cost.json'),
    ('arena.MatchLogTemplate', 'arena_match_log_template.json'),
    ('arena.SearchRange', 'arena_search_range.json'),
    ('arena.ResetCost', 'arena_reset_cost.json'),

    ('training_tower.TowerSaleGoods', 'tower_sale_goods.json'),
    ('training_tower.TowerStarReward', 'tower_star_reward.json'),
    ('training_tower.TowerRankReward', 'tower_rank_reward.json'),
    ('training_tower.TowerGameLevel', 'tower_level.json'),
    ('training_tower.TowerResetCost', 'tower_reset_cost.json'),

    ('territory.TerritoryBuilding', 'territory_building.json'),
    ('territory.StaffSpecialProduct', 'territory_staff_special_product.json'),
    ('territory.TerritoryInspireCost', 'territory_inspire_cost.json'),
    ('territory.ReportTemplate', 'territory_report_template.json'),
    ('territory.TerritoryStore', 'territory_store.json'),
    ('territory.Event', 'territory_event.json'),

    ('store.StoreCondition', 'store_condition.json'),
    ('store.StoreType', 'store_type.json'),
    ('store.Store', 'store.json'),
    ('store.StoreRefresh', 'store_refresh_cost.json'),

    ('collection.Collection', 'collection.json'),

    ('energy.BuyCost', 'energy_buy_cost.json'),

    ('formation.Slot', 'formation_slot.json'),
    ('formation.Formation', 'formation.json'),

    ('welfare.WelfareSignIn', 'welfare_signin.json'),
    ('welfare.WelfareNewPlayer', 'welfare_new_player.json'),
    ('welfare.WelfareLevelReward', 'welfare_level_reward.json'),

    ('union.UnionLevel', 'union_level.json'),
    ('union.UnionSignIn', 'union_signin.json'),
    ('union.UnionExplore', 'union_explore.json'),
    ('union.UnionExploreRankReward', 'union_explore_rank_reward.json'),
    ('union.UnionMemberExploreRankReward', 'union_member_explore_rank_reward.json'),
    ('union.UnionHarassBuyTimesCost', 'union_harass_buy_times_cost.json'),
    ('union.UnionSkill', 'union_skill.json'),

    ('purchase.PurchaseGoods', 'purchase_goods.json'),
    ('purchase.PurchaseYueka', 'purchase_yueka.json'),
    ('purchase.PurchaseFirstReward', 'purchase_first_reward.json'),

    ('activity.NewPlayerActivity', 'activity_new_player.json'),
    ('activity.DailyBuy', 'activity_daily_buy.json'),
    ('activity.OnlineTimeActivity', 'activity_online_time.json'),
    ('activity.ChallengeActivity', 'activity_challenge.json'),
    ('activity.PurchaseContinuesActivity', 'activity_purchase_continues.json'),
    ('activity.LevelGrowingActivity', 'activity_level_growing.json'),

    ('name.FirstName', 'first_name.json'),
    ('name.LastName', 'last_name.json'),

    ('plunder.BaseStationLevel', 'base_station_level.json'),
    ('plunder.PlunderIncome', 'plunder_income.json'),
    ('plunder.PlunderBuyTimesCost', 'plunder_buy_times_cost.json'),
    ('plunder.PlunderNPC', 'plunder_npc.json'),
    ('plunder.PlunderDayReward', 'plunder_daily_reward.json'),

    ('party.PartyLevel', 'party_level.json'),
    ('party.PartyBuyItem', 'party_buy_item.json'),
    ('party.PartyMessageTemplate', 'party_message_template.json'),

    ('championship.ChampionshipWinScore', 'championship_win_score.json'),
    ('championship.ChampionshipScoreReward', 'championship_score_reward.json'),
    ('championship.ChampionshipRankReward', 'championship_rank_reward.json'),
    ('championship.ChampionshipBet', 'championship_bet.json'),
)

class InMemoryZip(object):
    def __init__(self):
        self.buffer = StringIO()

    def add(self, filename, content):
        f = zipfile.ZipFile(self.buffer, mode='a', compression=zipfile.ZIP_DEFLATED)
        f.writestr(filename, content)

    def read(self):
        return self.buffer.getvalue()


def download_zip(request):
    memzip = InMemoryZip()
    for model, filename in MODELS:
        fixture = get_fixture(model)
        memzip.add(filename, fixture)

    now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    response = HttpResponse(memzip.read(), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="config_{0}.zip"'.format(now)
    return response
