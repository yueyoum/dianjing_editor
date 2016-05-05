# -*- coding:utf-8 -*-
from django.db import models


POSITION_TYPE = (
        (1, '在左边'),
        (2, '在右边')
    )


class TaskStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'task_status'
        verbose_name = '任务状态'
        verbose_name_plural = '任务状态'


class TaskType(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="类型id")
    name = models.CharField(unique=True, max_length=32, verbose_name="类型名")
    des = models.TextField(blank=True, verbose_name="类型描述")

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
    # 任务描述
    des = models.TextField(blank=True, verbose_name="任务描述")
    # next id
    next_task = models.IntegerField(default=0, verbose_name="下一个任务id")
    # 任务触发类型
    trigger = models.ForeignKey(TaskTrigger, null=True, blank=True, verbose_name="触发类型")
    # 触发值
    trigger_value = models.IntegerField(default=0, verbose_name="触发值")
    # 任务类型
    tp = models.ForeignKey(TaskType, verbose_name="任务类型")
    # 任务奖励
    reward = models.ForeignKey('package.Package', verbose_name="任务奖励")
    # 是否是客户端任务，比如点击NPC之类的
    client_task = models.BooleanField(default=False, verbose_name="是否是客户端任务")
    # 成功率， 这个是客户端操作的任务
    success_rate = models.IntegerField(default=100, verbose_name="成功率")
    # 是否是任务链首个
    task_begin = models.BooleanField(default=False, verbose_name="是否是任务链头")

    class Meta:
        db_table = "task"
        ordering = ('id',)
        verbose_name = "任务"
        verbose_name_plural = "任务"

    @classmethod
    def patch_fixture(cls, fixture):
        def make_target(target):
            return target.tp.id, target.param, target.value

        for f in fixture:
            pk = f['pk']
            targets = TaskTarget.objects.filter(task__id=pk)
            f['fields']['targets'] = [make_target(x) for x in targets]

        return fixture


class TaskTargetType(models.Model):
    MODE = (
        (1, "数值累加"),
        (2, "比较"),
    )

    COMPARE = (
        (1, ">="),
        (2, "<="),
    )

    id = models.IntegerField(primary_key=True, verbose_name="目标类型id")
    name = models.CharField(max_length=255, verbose_name="目标类型名")
    mode = models.IntegerField(choices=MODE, default=1, verbose_name="判断类型")
    compare_type = models.IntegerField(choices=COMPARE,default=1, verbose_name="比较方式")
    compare_source = models.CharField(max_length=255, blank=True, verbose_name="比较源", help_text="只有比较类型才需要设置")
    has_param = models.BooleanField(default=False, verbose_name="是否有目标参数")
    des = models.TextField(verbose_name="目标类型描述")

    # unicode显示名称
    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "target_type"
        verbose_name = "目标类型"
        verbose_name_plural = "目标类型"


class TaskTarget(models.Model):
    task = models.ForeignKey(Task, verbose_name="task_target")
    tp = models.ForeignKey(TaskTargetType, verbose_name="目标类型")
    param = models.IntegerField(default=0, verbose_name="目标参数")
    value = models.IntegerField(default=1, verbose_name="目标值")

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
