# -*- coding:utf-8 -*-
from django.db import models

POSITION_TYPE = (
        (1, '在左边'),
        (2, '在右边')
    )


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
    param = models.IntegerField(default=0)
    compare_type = models.CharField(max_length=32, default='>=')
    scene = models.CharField(max_length=255, blank=True)
    ui = models.CharField(max_length=255, blank=True)
    server_module = models.CharField(max_length=255, blank=True)
    time_limit = models.BooleanField(default=False)

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
