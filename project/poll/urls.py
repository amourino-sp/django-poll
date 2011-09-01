from django.conf.urls.defaults import patterns, url
from .views import QuestionDetailView, question_detail, question_list, question_add

urlpatterns = patterns('',
    url(r'^$', question_list, name='question_list'),
    url(r'^add$', question_add, name='question_add'),
    url(r'^(?P<slug>[\w-]+)$', QuestionDetailView.as_view(),
        name='question_detail'),
    # url(r'^(?P<slug>[\w-]+)$', question_detail, name='question_detail'),
)
