# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django.db import models
from django.utils.translation import ugettext_lazy as _


class CalendarEvent(models.Model):
    """
    Calendar Events
    """
    EVENT_TYPE_CHOICES = (
        ('', _('Normal')),
        ('event-warning', _('Warning')),
        ('event-info', _('Info')),
        ('event-success', _('Success')),
        ('event-inverse', _('Inverse')),
        ('event-special', _('Special')),
        ('event-important', _('Important')),
    )
    hash = models.UUIDField(blank=False, null=False, unique=False, db_index=True)
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    url = models.URLField(verbose_name=_('URL'), null=True, blank=True)
    type = models.CharField(blank=True, max_length=20, verbose_name=_('CSS Class'),
                            choices=EVENT_TYPE_CHOICES)
    start = models.DateTimeField(verbose_name=_('Start Date'), null=False, blank=False)
    end = models.DateTimeField(verbose_name=_('End Date'), null=False,
                               blank=False)

    @property
    def event_length(self):
        return self.end - self.start

    def __str__(self):
        return self.title
