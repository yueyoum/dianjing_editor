# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError

from apps.staff.models import Staff


class ChallengeType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='类型')
    level = models.IntegerField(verbose_name="等级")
    des = models.TextField(blank=True, verbose_name="描述")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'challenge_type'
        verbose_name = '挑战赛类型'
        verbose_name_plural = '挑战赛类型'


class ChallengeMatch(models.Model):
    id = models.IntegerField(primary_key=True)
    next_id = models.IntegerField(verbose_name="下一关ID")
    name = models.CharField(max_length=255, verbose_name="名字")
    tp = models.ForeignKey(ChallengeType, verbose_name="类型")
    policy = models.ForeignKey('unit.Policy', verbose_name="战术")

    level = models.IntegerField(verbose_name="选手等级")
    strength = models.FloatField(verbose_name="选手强度系数")

    staffs = models.CommaSeparatedIntegerField(max_length=255, verbose_name="选手ID列表")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'challenge_match'
        verbose_name = '挑战赛'
        verbose_name_plural = '挑战赛'


    def clean(self):
        staffs = [int(s) for s in self.staffs.split(',')]
        if len(staffs) != 5:
            raise ValidationError("wrong staffs")

        for s in staffs:
            if not Staff.objects.filter(id=int(s)).exists():
                raise ValidationError("Staff {0} not exists".format(s))

    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            staffs = f['fields']['staffs']
            f['fields']['staffs'] = [int(s) for s in staffs.split(',')]

        return fixture
