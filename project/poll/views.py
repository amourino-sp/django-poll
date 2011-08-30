# -*- coding: utf-8 -*-
from .models import Question, Option
from .forms import QuestionForm

from photologue.models import Photo

from django.conf import settings
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.template.defaultfilters import slugify


def question_detail(request, slug):
    if request.method == 'POST':
        post = request.POST.copy()
        id = post.get("option_id", 0)
        option = get_object_or_404(Option, id=id)
        option.vote()
        return redirect(option.question)
    else:
        try:
            question = Question.objects.get(slug=slug)
        except Question.DoesNotExist:
            raise Http404

        return render_to_response(
            'question_detail.html',
            {'question': question},
            context_instance=RequestContext(request))


def question_list(request):
    questions = Question.objects.all()
    return render_to_response('question_list.html',
                              {'questions': questions})


def question_add(request):
    form = QuestionForm()

    if request.method == 'POST':
        file_photo = request.FILES['photo']
        form = QuestionForm(request.POST, request.FILES)
        photo = Photo(image=handle_uploaded_file(file_photo),
                      title=file_photo.name,
                      title_slug=slugify(file_photo.name),)
        photo.save()
        form.photo = photo
        if form.is_valid():
            form.user = request.user
            question = form.save()
            return redirect(question)

    return render_to_response(
                'question_add.html',
                {'form': form},
                context_instance=RequestContext(request))


def handle_uploaded_file(f):
    path = ''.join((settings.STATIC_ROOT, f.name[f.name.rfind('/') + 1:]))
    destination = open(path, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)

    destination.close()
    return path
