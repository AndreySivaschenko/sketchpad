from django.conf.urls import url
from django.contrib import admin

from loginsys import views

urlpatterns =[
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^register/$', views.register),
]