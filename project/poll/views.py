from .models import Question, Option
from django.http import Http404
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, redirect
from poll.forms import QuestionForm
from photologue.models import Photo
from django.template.defaultfilters import slugify
from django.views.generic import DetailView

class QuestionDetailView(DetailView):
    context_object_name = "question"
    model = Question
    template_name = "question_detail.html"

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)

        context[self.context_object_name] = Question.objects.get(
                                                slug=self.kwargs['slug'],
                                            )
        return context


def question_detail(request, slug):
    """
    >>> a = ['larry', 'curly', 'moe']
    >>> question_detail(a, 0)
    'larry'
    >>> question_detail(a, 1)
    'curly'
    """
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
            {'question':question, },
            context_instance=RequestContext(request),
        )


def question_list(request):
    questions = Question.objects.all()
    return render_to_response(
                'question_list.html',
                {'questions': questions, },
    )


def question_add(request):

    form = QuestionForm()

    if request.method == 'POST':
        file_photo = request.FILES['photo']
        form = QuestionForm(request.POST, request.FILES)
        photo = Photo(image=handle_uploaded_file(file_photo),
                      title=file_photo.name,
                      title_slug=slugify(file_photo.name),
                )
        photo.save()
        form.photo = photo
        if form.is_valid():
            form.user = request.user
            question = form.save()
            return redirect(question)

    return render_to_response(
                'question_add.html',
                {'form': form, },
                context_instance=RequestContext(request),
    )


def handle_uploaded_file(f):
    path = ''.join(('/home/pablo/proyectos/clase/Encuesta/static/',
           f.name[f.name.rfind('/') + 1:]))
    destination = open(path, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)

    destination.close()
    return path
