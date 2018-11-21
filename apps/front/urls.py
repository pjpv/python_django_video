"""videsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include, url
from .views import IndexView
from subject.views import subjectView
from video.views import playView

urlpatterns = [
    url('^$', IndexView.as_view(), name='index'),
    url('s/(?P<id>\d+).html', subjectView.as_view(), name='subject'),
    url('(?P<id>\d+)/play.html', playView.as_view(), name='play'),
]
