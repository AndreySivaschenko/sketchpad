import datetime
from django import template
from django.contrib import auth
from django.shortcuts import render

from sketch.models import Note

register = template.Library()

@register.filter
def index(date, i):
    return date[int(i)]

