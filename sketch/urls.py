from django.conf.urls import url
from django.contrib import admin

from sketch import views

urlpatterns =[
    url(r'^note/$', views.note, name='note'),
    url(r'^add_note$', views.add_note, name='add'),
    url(r'^add/$', views.add),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^update/(?P<id>\d+)$', views.update),
    url(r'^delete/(?P<id>\d+)$', views.destroy),
    url(r'^profile/$', views.view_profile,name='profile'),
    url(r'^profile/edit/$', views.edit_profile,name='profile/edit'),
]