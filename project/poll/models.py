# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Question(models.Model):
    """
    Questions
    """
    user = models.ForeignKey(User, related_name='questions',
                             verbose_name=_('User'))
    question = models.CharField(_('Question'), max_length=30, unique=True)
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)
    order = models.PositiveIntegerField()
    slug = models.CharField(_('Slug'),max_length=100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.question)
        super(Question, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.question

    class Meta:
        # Question.objects.latest()
        get_latest_by = 'created_at'
        ordering = ['order']
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')


class Option(models.Model):
    """
    Options
    """
    question = models.ForeignKey(Question, related_name='options',
                                 verbose_name=_('Question'))
    answer = models.CharField(_('Answer'), max_length=30)
    votes = models.PositiveIntegerField(_('Votes'), default=0 )

    def __unicode__(self):
        return self.answer

    class Meta:
        verbose_name = _('Option')
        verbose_name_plural = _('Options')
