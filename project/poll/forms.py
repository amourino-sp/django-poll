# -*- coding: utf-8 -*-
from .models import Question

from django import forms


class QuestionForm(forms.ModelForm):

    photo = forms.ImageField()

    class Meta:
        model = Question
        exclude = ('slug', 'user')
