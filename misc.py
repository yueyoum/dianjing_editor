# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       misc
Date Created:   2016-04-22 14-36
Description:

"""
import json
from cStringIO import StringIO

import redis
from django.core import management

r = redis.Redis()

def make_cache_key(model):
    return 'dianjing:editor:cache:{0}'.format(model)

def cache_get(model):
    key = make_cache_key(model)
    return r.get(key)

def cache_set(model, data):
    key = make_cache_key(model)
    r.set(key, data)

def get_fixture(model):
    data = cache_get(model)
    if not data:
        data = create_fixture(model)
        cache_set(model, data)
        print "{0}\tGET FROM DB".format(model)
    else:
        print "{0}\tGET FROM CACHE".format(model)

    return data

def create_fixture(model):
    buf = StringIO()
    a, b = model.split('.')

    m = __import__('apps.{0}.models'.format(a), fromlist=[b])
    m = getattr(m, b)

    management.call_command('dumpdata', model, format='json', indent=4, stdout=buf)
    data = buf.getvalue()

    cf = getattr(m, 'patch_fixture', None)
    if cf:
        fixture = cf(json.loads(data))
        data = json.dumps(fixture, indent=2)

    return data
