# -*- coding: utf-8 -*-
from .views import question_detail, question_list, question_add

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', question_list, name='question_list'),
    url(r'^add$', question_add, name='question_add'),
    url(r'^(?P<slug>[\w-]+)$', question_detail, name='question_detail'),
)
