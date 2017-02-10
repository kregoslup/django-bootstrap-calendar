# -*- coding: utf-8 -*-
from rest_framework import serializers

from django_bootstrap_calendar.models import CalendarEvent

__author__ = 'sandlbn'


class EventSerializer(serializers.ModelSerializer):
    length = serializers.CharField(source='event_length')

    class Meta:
        model = CalendarEvent
        fields = ('hash', 'title', 'url', 'type', 'start', 'end', 'length')
