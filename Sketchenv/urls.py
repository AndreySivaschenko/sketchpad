"""Sketchenv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from registration.forms import RegistrationFormUniqueEmail
from registration.backends.default.views import RegistrationView


urlpatterns = [
    url(r'^admin/', include (admin.site.urls)),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^', include('landing.urls')),
    url('^user/', include('sketch.urls')),
    url(r'^accounts/register/$',RegistrationView.as_view(form_class=RegistrationFormUniqueEmail),
        name='registration_register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)