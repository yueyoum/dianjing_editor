# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError


# 活动大类
class ActivityCategory(models.Model):
    MODE = (
        (1, "手动领取"),
        (2, "系统邮件"),
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    mode = models.IntegerField(choices=MODE, verbose_name="奖励模式")

    fixed = models.BooleanField(default=False, verbose_name="固定活动",
                                help_text="固定活动不用设置下面的时间")

    start_at = models.DateTimeField(null=True, blank=True, verbose_name="开始时间")
    end_at = models.DateTimeField(null=True, blank=True, verbose_name="结束时间")

    des = models.TextField(verbose_name="描述")

    def __unicode__(self):
        return self.name

    def clean(self):
        if self.fixed:
            return

        if not self.start_at or not self.end_at:
            raise ValidationError("非固定活动需要设置时间")

    class Meta:
        db_table = 'activity_category'
        verbose_name = '活动分类'
        verbose_name_plural = '活动分类'


# 活动小条目
# 单独一个表是为了保证ID唯一
class Activity(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.ForeignKey(ActivityCategory, verbose_name="分类")
    name = models.CharField(max_length=255, verbose_name="名字")

    des = models.TextField(verbose_name="描述")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'activity'
        verbose_name = "活动"
        verbose_name_plural = "活动"


def _patch_activity_fixture(fixture):
    for f in fixture:
        activity_id = f['fields'].pop('activity')
        activity = Activity.objects.get(id=activity_id)
        f['pk'] = activity.id
        f['fields']['category'] = activity.category_id
        f['fields']['name'] = activity.name
        f['fields']['des'] = activity.des

    return fixture


# 签到活动
class ActivitySignIn(models.Model):
    activity = models.OneToOneField(Activity, verbose_name="活动")

    circle_package = models.ForeignKey('package.Package', null=True, verbose_name="大奖")

    mail_title = models.CharField(max_length=255, verbose_name="邮件标题")
    mail_content = models.TextField(verbose_name="邮件内容")

    class Meta:
        db_table = 'activity_signin'
        verbose_name = "活动 - 签到"
        verbose_name_plural = "活动 - 签到"

    @classmethod
    def patch_fixture(cls, fixture):
        fixture = _patch_activity_fixture(fixture)
        for f in fixture:
            day_reward = {}
            for _r in ActivitySignInDayReward.objects.filter(activity_signin__activity__id=f['pk']):
                day_reward[_r.day] = _r.package_id

            f['fields']['day_reward'] = day_reward

        return fixture


class ActivitySignInDayReward(models.Model):
    activity_signin = models.ForeignKey(ActivitySignIn)
    day = models.IntegerField(verbose_name="第几天")
    package = models.ForeignKey('package.Package', verbose_name="奖励")

    def __unicode__(self):
        return u"Day #{0}".format(self.day)

    class Meta:
        db_table = 'activity_signin_day_reward'


# 新玩家有礼： 登录给奖励
class ActivityLoginReward(models.Model):
    activity = models.ForeignKey(Activity, verbose_name="活动")
    day = models.IntegerField("第几天登录")
    package = models.ForeignKey('package.Package', verbose_name="奖励")

    class Meta:
        db_table = 'activity_login_reward'
        verbose_name = "活动 - 新玩家有礼"
        verbose_name_plural = "活动 - 新玩家有礼"

    @classmethod
    def patch_fixture(cls, fixture):
        return _patch_activity_fixture(fixture)
