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

    ('match.ChallengeChapter', 'challenge_chapter.json'),
    ('match.ChallengeMatch', 'challenge_match.json'),
    ('match.ChallengeGuide', 'challenge_guide.json'),
    ('match.Maps', 'maps.json'),

    ('building.Building', 'building.json'),

    ('task.Task', 'task.json'),
    ('task.TaskType', 'task_type.json'),
    ('task.TaskStatus', 'task_status.json'),
    ('task.TaskTargetType', 'task_target.json'),
    ('task.RandomEvent', 'random_event.json'),
    ('task.TaskMain', 'task_main.json'),


    ('notification.Notification', 'notification.json'),

    ('function.Function', 'function.json'),
    ('resources.Resource', 'resource.json'),

    ('emoticon.Emoticon', 'emoticon.json'),
    ('guide.Guide', 'guide.json'),
    ('template.SponsorLogTemplate', 'sponsor_template.json'),
    ('activity.ActivityCategory', 'activity_category.json'),
    ('activity.ActivitySignIn', 'activity_signin.json'),
    ('activity.ActivityLoginReward', 'activity_login_reward.json'),
    ('client_npc.ClientNPC', 'client_npc.json'),
    ('active_value.ActiveFunction', 'active_function.json'),
    ('active_value.ActiveReward', 'active_reward.json'),
    ('conversation.Conversation', 'conversation.json'),
    ('auction.Auction', 'auction.json'),

    ('item.ItemQuality', 'item_quality.json'),
    ('item.ItemNew', 'item_new.json'),
    ('item.ItemUse', 'item_use.json'),
    ('item.ItemMerge', 'item_merge.json'),
    ('item.EquipmentBase', 'equipment_new.json'),
    ('item.ItemExp', 'item_exp.json'),

    ('talent.Talent', 'talent.json'),
    ('vip.VIP', 'vip.json'),

    ('dungeon.Dungeon', 'dungeon.json'),
    ('dungeon.DungeonGrade', 'dungeon_grade.json'),

    ('npc.NPCFormation', 'npc_formation.json'),

    ('arena.ArenaNPC', 'arena_npc.json'),
    ('arena.HonorReward', 'arena_honor_reward.json'),
    ('arena.RankReward', 'arena_rank_reward.json'),
    ('arena.MatchReward', 'arena_match_reward.json'),
    ('arena.BuyTimesCost', 'arena_buy_times_cost.json'),
    ('arena.MatchLogTemplate', 'arena_match_log_template.json'),

    ('training_tower.TowerSaleGoods', 'sale_goods.json'),
    ('training_tower.TowerStarReward', 'tower_star_reward.json'),
    ('training_tower.TowerRankReward', 'tower_rank_reward.json'),
    ('training_tower.TowerGameLevel', 'tower_level.json'),
    ('training_tower.TowerResetCost', 'tower_reset_cost.json'),

    ('territory.TerritoryBuilding', 'territory_building.json'),
    ('territory.StaffSpecialProduct', 'territory_staff_special_product.json'),
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
