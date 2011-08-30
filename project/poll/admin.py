# -*- coding: utf-8 -*-
from .models import Question, Option

from django.contrib.admin import site, ModelAdmin, TabularInline, StackedInline
from django.utils.translation import ugettext as _


class OptionInline(StackedInline):
    model = Option
    extra = 4
    fields = ('answer',)


class QuestionAdmin(ModelAdmin):
    inlines = [OptionInline]
    list_display = ('question', 'order', 'count_options',)
    list_editable = ('order',)
    actions_on_bottom = True
    #filter_vertical = ('user',)
    raw_id_fields = ('user',)

    def count_options(self, question):
        return question.options.all().count()
    count_options.short_description = _('Counter')


class OptionAdmin(ModelAdmin):
    list_display = ('question', 'answer', 'votes',)
    fields = ('question', 'answer',)


site.register(Question, QuestionAdmin)
site.register(Option, OptionAdmin)
