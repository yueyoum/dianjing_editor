# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       signal_handler
Date Created:   2016-04-22 14-53
Description:

"""

from django.dispatch import receiver
from django.db.models.signals import post_save

from import_export.signals import post_import

from misc import cache_set, create_fixture


@receiver(post_import, dispatch_uid='xxx.post_import')
def _post_import(model, **kwargs):
    related_model_getter = getattr(model, 'get_related_model', None)
    if related_model_getter:
        model = related_model_getter()

    key_func = getattr(model, 'get_fixture_key', None)
    if key_func:
        # 期望cache住
        key = key_func()

        data = create_fixture(key, model)
        cache_set(key, data)


@receiver(post_save, dispatch_uid='xxx.post_save')
def _post_save(sender, **kwargs):
    related_model_getter = getattr(sender, 'get_related_model', None)
    if related_model_getter:
        sender = related_model_getter()

    key_func = getattr(sender, 'get_fixture_key', None)
    if key_func:
        # 期望cache住
        key = key_func()

        data = create_fixture(key, sender)
        cache_set(key, data)
