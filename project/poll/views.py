# -*- coding: utf-8 -*-
from .models import Question, Option
from django.http import HttpResponse, Http404

def question_detail(request, slug):
    try:
        question = Question.objects.get(slug=slug)
    except Question.DoesNotExist:
        raise Http404

def question_list(request):
    questions = Question.objects.all()
    return HttpResponse()
