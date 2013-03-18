from django.contrib import admin
from events.models import Event
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.contenttypes import generic


class EventAdmin(admin.ModelAdmin):

    list_display = ('when', 'what',)
    # content_object = generic.GenericForeignKey("content_type", "object_id")
    date_hierarchy = 'when'

admin.site.register(Event, EventAdmin, )
