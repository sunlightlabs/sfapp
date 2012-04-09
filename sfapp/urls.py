from django.conf.urls import patterns, include, url

from sfapp.views import SubscribeView

urlpatterns = patterns('',
    url(r'^subscribe/$', SubscribeView.as_view()),
)
