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

r = redis.Redis(db=1)

def make_cache_key(model):
    return 'dianjing:editor:cache:{0}'.format(model)

def get_model_instance(model):
    a, b = model.split('.')
    m = __import__('apps.{0}.models'.format(a), fromlist=[b])
    return getattr(m, b)

def cache_get(model):
    key = make_cache_key(model)
    return r.get(key)

def cache_set(model, data):
    key = make_cache_key(model)
    r.set(key, data)

def get_fixture(model):
    ins = get_model_instance(model)
    key_func = getattr(ins, 'get_fixture_key', None)
    if not key_func:
        # 对应的model没有这个方法
        return create_fixture(model, ins)

    # 加了的，就是期望走cache的
    data = cache_get(model)
    if not data:
        data = create_fixture(model, ins)
        cache_set(model, data)
    else:
        print "GET FROM CACHE\t{0}".format(model)

    return data

def create_fixture(model, ins):
    buf = StringIO()
    management.call_command('dumpdata', model, format='json', indent=4, stdout=buf)
    data = buf.getvalue()

    cf = getattr(ins, 'patch_fixture', None)
    if cf:
        fixture = cf(json.loads(data))
        data = json.dumps(fixture, indent=2)

    print "GET FROM MYSQL\t{0}".format(model)
    return data

def parse_text(text, num):
    res = []
    for x in text.split(';'):
        if not x:
            continue

        xlist = x.split(',')

        item = []
        for i in xlist[:num]:
            item.append(int(i))
        res.append(item)

    return res

def parse_text_split_by_comma(text):
    res = []
    for x in text.split(','):
        if not x:
            continue

        res.append(int(x))

    return res