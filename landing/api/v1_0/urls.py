from django.conf.urls import url
from django.contrib import admin

from .view import (
    UserCreateAPIView,
    UserLoginAPIView

)

urlpatterns =[
    url(r'^log/$', UserLoginAPIView.as_view(), name='login'),
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
]