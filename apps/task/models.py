# -*- coding:utf-8 -*-
from django.db import models


POSITION_TYPE = (
        (1, '在左边'),
        (2, '在右边')
    )


class TaskStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    # icon = models.CharField(max_length=255)

    class Meta:
        db_table = 'task_status'
        verbose_name = '任务状态'
        verbose_name_plural = '任务状态'


class TaskType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="类型id")
    name = models.CharField(unique=True, max_length=32, verbose_name="类型名")
    # des = models.TextField(default=None, verbose_name="类型描述")

    # unicode显示名称
    def __unicode__(self):
        return u"{0} : {1}".format(self.name, self.id)

    class Meta:
        db_table = "task_type"
        verbose_name = "任务类型"
        verbose_name_plural = "任务类型"


class TaskTrigger(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="触发类型id")
    name = models.CharField(unique=True, max_length=255, verbose_name="触发类型名")

    # unicode显示名称
    def __unicode__(self):
        return u"{0} : {1}".format(self.name, self.id)

    class Meta:
        db_table = "task_trigger"
        verbose_name = "任务触发"
        verbose_name_plural = "任务触发"


class Task(models.Model):
    # 任务id
    id = models.IntegerField(primary_key=True, verbose_name="任务id")
    # 任务名称
    name = models.CharField(max_length=32, verbose_name="任务名")
    # next id
    next_task = models.IntegerField(default=0, verbose_name="下一个任务id")
    # 任务触发类型
    trigger_tp = models.ForeignKey(TaskTrigger, verbose_name="触发类型")
    # 触发值
    trigger_rate = models.IntegerField(default=0, verbose_name="触发值")
    # 任务类型
    tp = models.ForeignKey(TaskType, verbose_name="任务类型")
    # 任务奖励
    reward = models.ForeignKey('package.Package', verbose_name="任务奖励")
    # 是否是客户端任务，比如点击NPC之类的
    client_task = models.BooleanField(default=False, verbose_name="是否是客户端任务")
    # 成功率， 这个是客户端操作的任务
    success_rate = models.IntegerField(default=100, verbose_name="成功率")

    class Meta:
        db_table = "task"
        ordering = ('id',)
        verbose_name = "任务"
        verbose_name_plural = "任务"

    @classmethod
    def patch_fixture(cls, fixture):
        def make_target(target):
            return {
                'tp_id': target.tp,
                'tp_num': target.value,
            }

        for f in fixture:
            pk = f['pk']
            targets = TaskTarget.objects.filter(task__id=pk)

            f['fields']['target'] = [make_target(x) for x in targets]

            if not f['fields']['reward']:
                f['fields']['reward'] = 0

        return fixture


class TaskTargetType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="目标类型id")
    name = models.CharField(max_length=255, verbose_name="目标类型名")

    # unicode显示名称
    def __unicode__(self):
        return u"{0} : {1}".format(self.name, self.id)

    class Meta:
        db_table = "target_type"
        verbose_name = "目标类型"
        verbose_name_plural = "目标类型"


class TaskTarget(models.Model):
    task = models.ForeignKey(Task, verbose_name="task_target")
    tp = models.ForeignKey(TaskTargetType, verbose_name="目标类型")
    value = models.IntegerField(default=1, verbose_name="目标类型值")

    class Meta:
        db_table = "task_target"
        verbose_name = "任务目标"
        verbose_name_plural = "任务目标"


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

