# -*- coding: utf-8 -*-

from django.db import models

from misc import cache_set, create_fixture


class ErrorMsg(models.Model):
    id = models.IntegerField(primary_key=True)
    error_index = models.CharField(max_length=64, unique=True)
    text_zh = models.CharField(max_length=255)
    is_retry = models.BooleanField(default=True)

    des = models.CharField(max_length=255, default="", blank=True)

    class Meta:
        db_table = 'error_msg'
        verbose_name = '错误代码'
        verbose_name_plural = '错误代码'

    @classmethod
    def get_fixture_key(cls):
        return 'errormsg.ErrorMsg'

    def save(self, **kwargs):
        super(ErrorMsg, self).save(**kwargs)
        key_func = getattr(self, 'get_fixture_key', None)
        if key_func:
            # 期望cache住
            key = key_func()

            data = create_fixture(key, self)
            cache_set(key, data)
