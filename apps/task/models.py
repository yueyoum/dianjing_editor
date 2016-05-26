# -*- coding:utf-8 -*-
from django.db import models


POSITION_TYPE = (
        (1, '在左边'),
        (2, '在右边')
    )


class RandomEvent(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='名字')
    icon = models.CharField(max_length=255, verbose_name='图标')
    level_min = models.IntegerField(default=1, verbose_name='最低等级')
    level_max = models.IntegerField(default=1, verbose_name='最高等级')
    trig_name = models.CharField(max_length=255, verbose_name='触发节点')
    package = models.ForeignKey('package.Package', verbose_name='奖励')

    class Meta:
        db_table = 'random_event'
        verbose_name = '随机事件'
        verbose_name_plural = '随机事件'

    @classmethod
    def patch_fixture(cls, fixture):
        def make_dialog(dialog):
            return {
                'position': dialog.position,
                'icon': dialog.icon,
                'dialog': dialog.dialog
            }

        for f in fixture:
            pk = f['pk']
            dialog_before = RandomEventDialogBefore.objects.filter(random_event__id=pk)
            dialog_after = RandomEventDialogAfter.objects.filter(random_event__id=pk)

            f['fields']['dialog_before'] = [make_dialog(x) for x in dialog_before]
            f['fields']['dialog_after'] = [make_dialog(x) for x in dialog_after]

            if not f['fields']['package']:
                f['fields']['package'] = 0

        return fixture


class RandomEventDialogBefore(models.Model):
    random_event = models.ForeignKey(RandomEvent, related_name='dialog_before')
    position = models.IntegerField(choices=POSITION_TYPE, verbose_name='对话者位置')
    icon = models.CharField(max_length=255, verbose_name='对话者图标')
    dialog = models.TextField()

    class Meta:
        db_table = 'random_event_dialog_before'
        verbose_name = '随机事件前对话'
        verbose_name_plural = '随机事件前对话'


class RandomEventDialogAfter(models.Model):
    random_event = models.ForeignKey(RandomEvent, related_name='dialog_after')
    position = models.IntegerField(choices=POSITION_TYPE, verbose_name='对话者位置')
    icon = models.CharField(max_length=255, verbose_name='对话者图标')
    dialog = models.TextField()

    class Meta:
        db_table = 'random_event_dialog_after'
        verbose_name = '随机事件后对话'
        verbose_name_plural = '随机事件后对话'


class TaskMain(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    des = models.TextField()
    challenge_id = models.IntegerField()
    items = models.CharField(max_length=255)

    class Meta:
        db_table = 'task_main'
        verbose_name = '主线任务'
        verbose_name_plural = '主线任务'

    @classmethod
    def patch_fixture(cls, fixture):
        def parse_items(items):
            result = []
            for x in items.split(';'):
                if not x:
                    continue

                _id, _amount  = x.split(',')
                result.append((int(_id), int(_amount)))

            return result

        for f in fixture:
            f['fields']['items'] = parse_items(f['fields']['items'])

        return fixture


class TaskCondition(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    ui = models.CharField(max_length=255)

    class Meta:
        db_table = 'task_condition'
        verbose_name = '任务条件'
        verbose_name_plural = '任务条件'


class TaskDaily(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    des = models.TextField()
    club_level = models.IntegerField()
    vip_level = models.IntegerField()

    condition_id = models.IntegerField()
    condition_value = models.IntegerField()
    rewards = models.TextField(help_text='id,amount;id,amount;...')

    class Meta:
        db_table = 'task_daily'
        verbose_name = '日常任务'
        verbose_name_plural = '日常任务'


    @classmethod
    def patch_fixture(cls, fixture):
        def _parse(text):
            result = []
            for x in text.split(';'):
                if not x:
                    continue

                _id, _amount = x.split(',')
                result.append((int(_id), int(_amount)))

            return result

        for f in fixture:
            f['fields']['rewards'] = _parse(f['fields']['rewards'])

        return fixture
