#!/usr/bin/env python
import os
import sys

from django.conf import settings, global_settings
from django.conf.urls import patterns
from django.core.management import call_command

PWD = os.path.abspath(os.path.dirname(__file__))
sys.path.append(PWD)


try:
    HOST = sys.argv[1]
except IndexError:
    HOST = '127.0.0.1:8000'


def index(request):
    from django.shortcuts import render
    return render(request, 'sfapp/_demo.html')

urlpatterns = patterns('',
    (r'^$', index),
)


class DemoSettings(object):

    DEBUG = True
    TEMPLATE_DEBUG = DEBUG

    SECRET_KEY = 'Wvr32LrQ2mchbA7SUdBiy5Vy/UoauUJ/m6tlzP1woIE='

    INSTALLED_APPS = (
        'django.contrib.staticfiles',
        'sfapp',
    )

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(PWD, 'static-root')
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    ROOT_URLCONF = 'demo'

    def __getattr__(self, name):
        return getattr(global_settings, name)


if __name__ == '__main__':

    demo_settings = DemoSettings()
    settings.configure(demo_settings)

    call_command('runserver', HOST)
