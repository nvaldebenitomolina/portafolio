"""portafolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import portafolio.project1
from django.views.generic import TemplateView
from django.conf.urls import url
from portafolio import views

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    url('^project1$', views.project1, name="project1"),
    path('project2', views.project2, name='project2'),
    path('project3', views.project3, name='project3'),
    path('project4', views.project4, name='project4'),
    path('project5', views.project5, name='project5'),
    path('project6', views.project6, name='project6'),
    path('challenge1', views.challenge1, name='challenge1'),
    path('challenge2', views.challenge2, name='challenge2'),
    path('challenge3', views.challenge3, name='challenge3'),
    path('challenge4', views.challenge4, name='challenge4'),
    path('challenge5', views.challenge5, name='challenge5'),
]

urlpatterns += staticfiles_urlpatterns()