# -*- coding: utf-8 -*-
from django.db.models.query_utils import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django_bootstrap_calendar.models import CalendarEvent

__author__ = 'sandlbn'


class EventSerializer(serializers.ModelSerializer):
    length = serializers.CharField(source='event_length')

    class Meta:
        model = CalendarEvent
        fields = ('hash', 'title', 'url', 'type', 'start', 'end', 'length')

    def date_clashes(self, start, end):
        return CalendarEvent.objects.filter(
            Q(start__range=(start, end) | Q(end__range=(start, end)))).exists()

    def validate(self, attrs):
        start = attrs.get('start', None)
        end = attrs.get('end', None)
        if start and end and self.date_clashes(start, end):
            raise ValidationError({'Invalid date'})
        return super(EventSerializer, self).validate(attrs)
