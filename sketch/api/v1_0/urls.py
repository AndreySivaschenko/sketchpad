from django.conf.urls import url
from django.contrib import admin

from .views import (NoteListApiView)

urlpatterns =[
    url(r'^note/$', NoteListApiView.as_view(), name='note'),
]