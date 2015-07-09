# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError

class StaffRace(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=32, verbose_name="名称")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'staff_race'
        verbose_name = "种族"
        verbose_name_plural = "种族"


class StaffQuality(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    color = models.CharField(max_length=32)

    def __unicode__(self):
        return self.id

    class Meta:
        db_table = "staff_quality"
        verbose_name = "品质"
        verbose_name_plural = "品质"


class StaffStatus(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32, verbose_name="名称")
    value = models.IntegerField(verbose_name="加成值", help_text="5% 直接填5")
    des = models.CharField(max_length=255, verbose_name="说明", blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'staff_status'
        verbose_name = "状态"
        verbose_name_plural = "状态"



class Staff(models.Model):
    BUY_TYPE = (
        (1, "RMB"),
        (2, "钻石")
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=32, verbose_name="名字")
    avatar = models.CharField(max_length=32, verbose_name="头像")
    nation = models.CharField(max_length=32, verbose_name="国籍")

    race = models.ForeignKey(StaffRace, db_column='race', verbose_name="种族")
    quality = models.ForeignKey(StaffQuality, db_column='quality', verbose_name="品质")

    buy_type = models.IntegerField(choices=BUY_TYPE, verbose_name="签约费类型")
    buy_cost = models.IntegerField(verbose_name="签约费")
    can_recruit = models.BooleanField(verbose_name="是否可以招募", default=True)

    des = models.TextField(blank=True, verbose_name="简介")

    jingong = models.IntegerField(verbose_name="进攻")
    jingong_grow = models.FloatField(verbose_name="进攻成长")

    qianzhi = models.IntegerField(verbose_name="牵制")
    qianzhi_grow = models.FloatField(verbose_name="牵制成长")

    xintai = models.IntegerField(verbose_name="心态")
    xintai_grow = models.FloatField(verbose_name="心态成长")

    baobing = models.IntegerField(verbose_name="暴兵")
    baobing_grow = models.FloatField(verbose_name="暴兵成长")

    fangshou = models.IntegerField(verbose_name="防守")
    fangshou_grow = models.FloatField(verbose_name="防守成长")

    yunying = models.IntegerField(verbose_name="运营")
    yunying_grow = models.FloatField(verbose_name="运营成长")

    yishi = models.IntegerField(verbose_name="意识")
    yishi_grow = models.FloatField(verbose_name="意识成长")

    caozuo = models.IntegerField(verbose_name="操作")
    caozuo_grow = models.FloatField(verbose_name="操作成长")


    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'staff'
        verbose_name = "员工"
        verbose_name_plural = "员工"


class StaffHot(models.Model):
    id = models.OneToOneField(Staff, primary_key=True, verbose_name="员工")
    cost = models.IntegerField(verbose_name="花费")

    class Meta:
        db_table = "staff_hot"
        verbose_name = "员工招募-人气王"
        verbose_name_plural = "员工招募-人气王"


class StaffRecruitSettings(models.Model):
    recruit = models.ForeignKey('StaffRecruit')
    quality = models.ForeignKey(StaffQuality, verbose_name="品质")
    first_amount = models.IntegerField(verbose_name="首次刷新出现次数")
    lucky_amount = models.IntegerField(verbose_name="幸运刷新出现次数")
    normal_amount = models.IntegerField(verbose_name="平时出现次数")


    class Meta:
        db_table = 'staff_recruit_settings'
        unique_together = (('recruit', 'quality'),)


class StaffRecruit(models.Model):
    COST_TYPE = (
        (1, "RMB"),
        (2, "钻石")
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    cost_type = models.IntegerField(choices=COST_TYPE, verbose_name="花费类型")
    cost_value = models.IntegerField(verbose_name="花费金额")
    lucky_times = models.IntegerField(verbose_name="幸运次数")

    des = models.TextField(blank=True, verbose_name="描述")

    recruit_settings = models.ManyToManyField(StaffRecruitSettings)


    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'staff_recruit'
        verbose_name = "员工招募-合约"
        verbose_name_plural = "员工招募-合约"


