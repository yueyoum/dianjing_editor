# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       signal_handler
Date Created:   2016-04-22 14-53
Description:

"""

from django.db.models.signals import post_save
from django.dispatch import receiver

from import_export.signals import post_import

from misc import cache_set, create_fixture

# from apps.errormsg.models import ErrorMsg


@receiver(post_import, dispatch_uid='post_import')
def _post_import(model, **kwargs):
    key_func = getattr(model, 'get_fixture_key', None)
    if key_func:
        # 期望cache住
        key = key_func()

        data = create_fixture(key, model)
        cache_set(key, data)


@receiver(post_save, dispatch_uid='post_save')
def _post_save(sender, **kwargs):
    _post_import(sender, **kwargs)

