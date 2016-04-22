# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       signal_handler
Date Created:   2016-04-22 14-53
Description:

"""

from django.dispatch import receiver

from import_export.signals import post_import

from misc import cache_set, create_fixture

@receiver(post_import, dispatch_uid='post_import')
def _post_import(model, **kwargs):
    key_func = getattr(model, 'get_fixture_key', None)
    if key_func:
        # 期望cache住
        key = key_func()

        data = create_fixture(key, model)
        cache_set(key, data)
