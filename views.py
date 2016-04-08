# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       views
Date Created:   2015-04-23 16:42
Description:

"""
import datetime
import json

from cStringIO import StringIO
import zipfile

from django.http import HttpResponse
from django.core import management

MODELS = (
    ('config.ClientConfig', 'client_config.json'),
    ('config.GlobalConfig', 'global_config.json'),
    ('errormsg.ErrorMsg', 'errormsg.json'),
    ('staff.StaffQuality', 'staff_quality.json'),
    ('staff.StaffRace', 'staff_race.json'),
    ('staff.StaffStatus', 'staff_status.json'),
    ('staff.StaffLevel', 'staff_level.json'),
    ('staff.Staff', 'staff.json'),
    ('staff.StaffHot', 'staff_hot.json'),
    ('staff.StaffRecruit', 'staff_recruit.json'),
    ('staff.StaffNew', 'staff_new.json'),
    ('staff.StaffLevelNew', 'staff_level_new.json'),
    ('staff.StaffStar', 'staff_star.json'),
    ('staff.StaffEquipmentQualityAddition', 'staff_equip_quality_addition.json'),
    ('staff.StaffEquipmentLevelAddition', 'staff_equip_level_addition.json'),
    ('training.TrainingProperty', 'training_property.json'),
    ('npc.NPCClub', 'npc_club.json'),
    ('npc.NPCClubName', 'npc_club_name.json'),
    ('npc.NPCManagerName', 'npc_manager_name.json'),
    ('unit.Unit', 'unit.json'),
    ('unit.Policy', 'policy.json'),
    ('unit.UnitEffect', 'unit_effect.json'),
    ('unit.UnitNew', 'unit_new.json'),
    ('unit.UnitLevelAddition', 'unit_level_addition.json'),
    ('unit.UnitStepAddition', 'unit_step_addition.json'),
    ('unit.UnitUnLock', 'unit_unlock.json'),
    ('skill.SkillType', 'skill_type.json'),
    ('skill.SkillCategory', 'skill_category.json'),
    ('skill.SkillAddition', 'skill_addition.json'),
    ('skill.Skill', 'skill.json'),
    ('skill.SkillWashCost', 'skill_wash_cost.json'),
    ('skill.Buff', 'skill_buff.json'),
    ('skill.TalentSkill', 'talent_skill.json'),
    ('club.ClubFlag', 'club_flag.json'),
    ('club.ClubLevel', 'club_level.json'),
    ('club.TibuSlot', 'tibu_slot.json'),
    ('qianban.QianBan', 'qianban.json'),
    ('match.ChallengeChapter', 'challenge_chapter.json'),
    ('match.ChallengeMatch', 'challenge_match.json'),
    ('match.MatchConversationStart', 'match_conversation_start.json'),
    ('match.MatchConversationEnd', 'match_conversation_end.json'),
    ('match.MatchConversationRoundEnd', 'match_conversation_round_end.json'),
    ('match.Maps', 'maps.json'),
    ('match.TrainingMatchReward', 'training_match_reward.json'),
    ('match.TrainingMatchScoreStore', 'training_match_store.json'),
    ('match.EliteArea', 'elite_area.json'),
    ('match.EliteMatch', 'elite_match.json'),
    ('package.Package', 'package.json'),
    ('building.Building', 'building.json'),
    ('building.Shop', 'business_shop.json'),
    ('building.Sponsor', 'business_sponsor.json'),
    ('building.BusinessBroadcastReward', 'business_broadcast_reward.json'),
    ('task.Task', 'task.json'),
    ('task.TaskType', 'task_type.json'),
    ('task.TaskStatus', 'task_status.json'),
    ('task.TaskTargetType', 'task_target.json'),
    ('task.RandomEvent', 'random_event.json'),
    ('notification.Notification', 'notification.json'),
    ('league.League', 'league.json'),
    ('function.Function', 'function.json'),
    ('resources.Resource', 'resource.json'),
    ('ladder.LadderLogTemplate', 'ladder_log_template.json'),
    ('ladder.LadderRankReward', 'ladder_rank_reward.json'),
    ('ladder.LadderScoreStore', 'ladder_score_store.json'),
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
    ('item.Item', 'item.json'),
    ('item.ItemQuality', 'item_quality.json'),
    ('item.Equipment', 'equipment.json'),
    ('item.ItemNew', 'item_new.json'),
    ('item.ItemUse', 'item_use.json'),
    ('item.ItemMerge', 'item_merge.json'),
    ('item.EquipmentBase', 'equipment_new.json'),
    ('item.ItemExp', 'item_exp.json'),
)


class InMemoryZip(object):
    def __init__(self):
        self.buffer = StringIO()

    def add(self, filename, content):
        f = zipfile.ZipFile(self.buffer, mode='a', compression=zipfile.ZIP_DEFLATED)
        f.writestr(filename, content)

    def read(self):
        return self.buffer.getvalue()


def create_fixture(model):
    buf = StringIO()
    a, b = model.split('.')

    m = __import__('apps.{0}.models'.format(a), fromlist=[b])
    m = getattr(m, b)

    management.call_command('dumpdata', model, format='json', indent=4, stdout=buf)
    data = buf.getvalue()

    cf = getattr(m, 'patch_fixture', None)
    if cf:
        fixture = cf(json.loads(data))
        data = json.dumps(fixture, indent=2)

    # return data.decode('unicode-escape').encode('utf-8')
    return data


def download_zip(request):
    memzip = InMemoryZip()
    for model, filename in MODELS:
        fixture = create_fixture(model)
        memzip.add(filename, fixture)

    now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    response = HttpResponse(memzip.read(), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="config_{0}.zip"'.format(now)
    return response
