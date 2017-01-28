from django.conf.urls import url
from django.contrib import admin

from sketch import views

urlpatterns =[
    url(r'^$', views.note, name='note'),
    url(r'^main$', views.main),
    url(r'^add_note$', views.add_note, name='add'),
    url(r'^add$', views.add),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^update/(?P<id>\d+)$', views.update),
    url(r'^delete/(?P<id>\d+)$', views.destroy)
]