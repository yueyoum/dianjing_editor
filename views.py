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
    ('errormsg.ErrorMsg', 'errormsg.json'),
    ('staff.StaffQuality', 'staff_quality.json'),
    ('staff.StaffRace', 'staff_race.json'),
    ('staff.StaffStatus', 'staff_status.json'),
    ('staff.StaffLevel', 'staff_level.json'),
    ('staff.Staff', 'staff.json'),
    ('staff.StaffHot', 'staff_hot.json'),
    ('staff.StaffRecruit', 'staff_recruit.json'),
    ('training.TrainingProperty', 'training_property.json'),
    ('training.TrainingSkill', 'training_skill_item.json'),
    ('npc.NPCClub', 'npc_club.json'),
    ('npc.NPCClubName', 'npc_club_name.json'),
    ('npc.NPCManagerName', 'npc_manager_name.json'),
    ('unit.Unit', 'unit.json'),
    ('unit.Policy', 'policy.json'),
    ('skill.SkillType', 'skill_type.json'),
    ('skill.SkillCategory', 'skill_category.json'),
    ('skill.SkillAddition', 'skill_addition.json'),
    ('skill.Skill', 'skill.json'),
    ('club.ClubFlag', 'club_flag.json'),
    ('club.ClubLevel', 'club_level.json'),
    ('qianban.QianBan', 'qianban.json'),
    ('match.ChallengeType', 'challenge_type.json'),
    ('match.ChallengeMatch', 'challenge_match.json'),
    ('match.MatchConversationStart', 'match_conversation_start.json'),
    ('match.MatchConversationEnd', 'match_conversation_end.json'),
    ('match.MatchConversationRoundEnd', 'match_conversation_round_end.json'),
    ('package.Package', 'package.json'),
    ('building.Building', 'building.json'),
    ('building.Shop', 'shop.json'),
    ('building.Sponsor', 'sponsor.json'),
    ('task.Task', 'task.json'),
    ('task.TaskType', 'task_type.json'),
    ('task.TaskStatus', 'task_status.json'),
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
    ('item.Item', 'item.json'),
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
    buffer = StringIO()
    a, b = model.split('.')

    m = __import__('apps.{0}.models'.format(a), fromlist=[b])
    m = getattr(m, b)

    management.call_command('dumpdata', model, format='json', indent=4, stdout=buffer)
    data = buffer.getvalue()

    cf = getattr(m ,'patch_fixture', None)
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
