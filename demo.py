#!/usr/bin/env python
import os
import sys

from django.conf.urls import *

PWD = os.path.abspath(os.path.dirname(__file__))

try:
    HOST = sys.argv[1]
except IndexError:
    HOST = '127.0.0.1:8000'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

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


# configure urls
urlpatterns = patterns('django.views.generic.simple',
    (r'^$', 'direct_to_template', {'template': 'sfapp/_demo.html'}),
)


def bootstrap():

    from django.core.management import call_command

    # add current directory to path
    sys.path.append(PWD)

    os.environ['DJANGO_SETTINGS_MODULE'] = 'demo'

    call_command('runserver', HOST)


if __name__ == '__main__':
    bootstrap()
