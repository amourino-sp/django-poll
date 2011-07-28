# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url
from .views import question_detail, question_list

urlpatterns = patterns('',
    url(r'^$', question_list, name='question_list'),
    url(r'^(?P<slug>[\w-]+)$', question_detail, name='question_detail'),
)
