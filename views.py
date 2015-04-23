# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       views
Date Created:   2015-04-23 16:42
Description:

"""
import datetime

from cStringIO import StringIO
import zipfile

from django.http import HttpResponse
from django.core import management


class InMemoryZip(object):
    def __init__(self):
        self.buffer = StringIO()

    def add(self, filename, content):
        f = zipfile.ZipFile(self.buffer, mode='a')
        f.writestr(filename, content)

    def read(self):
        return self.buffer.getvalue()



def create_fixture(model):
    buffer = StringIO()
    management.call_command('dumpdata', model, format='json', indent=4, stdout=buffer)
    return buffer.getvalue()


def download_zip(request):
    models = [
        ('errormsg.ErrorMsg', 'errormsg.json'),
    ]

    memzip = InMemoryZip()
    for model, filename in models:
        fixture = create_fixture(model)
        memzip.add(filename, fixture)

    now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%m-%S")

    response = HttpResponse(memzip.read(), content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="config_{0}.zip"'.format(now)
    return response
