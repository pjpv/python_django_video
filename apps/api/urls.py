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
    1. lude() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from subject.views import SubjectViewSet
from line.views import LineViewSet
from video.views import VideoViewSet
from category.views import CategoryViewSet

from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter()
router.register(r'categorys', CategoryViewSet, base_name="categorys")
router.register(r'subjects', SubjectViewSet, base_name="subjects")
router.register(r'lines', LineViewSet, base_name="lines")
router.register(r'videos', VideoViewSet, base_name="videos")
urlpatterns = router.urls

# urlpatterns = [
#     url(r'categorys/$',CategoryListView.as_view(), name='category-list'),
#     url(r'subjects/$',SubjectListView.as_view(), name='subjtct-list'),
# ]
# urlpatterns = [
#
#     url(r'', include(router.urls)),
# ]
