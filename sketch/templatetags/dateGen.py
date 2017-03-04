import datetime
from django import template
from django.contrib import auth
from django.shortcuts import render

from sketch.models import Note

register = template.Library()

@register.inclusion_tag('sketch/note.html')
def noteView(notes):
    notes = Note.objects.all()
    return {
        'noteVeiw':notes
    }

@register.filter
def index(date, i):
    return date[int(i)]

