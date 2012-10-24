from django.conf.urls import patterns, include, url
from django.views.decorators.csrf import csrf_exempt

from sfapp.views import SubscribeView

urlpatterns = patterns('',
    url(r'^subscribe/$', csrf_exempt(SubscribeView.as_view())),
)
