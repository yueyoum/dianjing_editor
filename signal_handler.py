# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       signal_handler
Date Created:   2016-04-22 14-53
Description:

"""

from django.dispatch import receiver

from import_export.signals import post_import

from apps.vip.models import VIP
from apps.staff.models import StaffNew
from apps.unit.models import UnitNew
from apps.item.models import ItemNew

from misc import cache_set, create_fixture

@receiver(post_import, dispatch_uid='post_import')
def _post_import(model, **kwargs):
    if isinstance(model, VIP):
        key = 'vip.VIP'
    elif isinstance(model, StaffNew):
        key = 'staff.StaffNew'
    elif isinstance(model, UnitNew):
        key = 'unit.UnitNew'
    elif isinstance(model, ItemNew):
        key = 'item.ItemNew'
    else:
        raise TypeError("error model instance: {0}".format(model))

    data = create_fixture(key)
    cache_set(key, data)
