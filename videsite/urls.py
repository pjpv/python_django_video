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
from django.conf import settings
from django.contrib.staticfiles.views import serve
from django.views.generic import TemplateView

# rest framework 文档
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('admin/', admin.site.urls),

    # rest_framework auth
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^docs/', include_docs_urls(title='zfdev movie')), # rest framework 文档

    # API
    url('api/', include('api.urls'), name='api'),

    # url('^(?P<path>crossdomain.xml)$', serve, name='crossdomain'),

    # vue 前端
    url('^v/',TemplateView.as_view(template_name='index_prod.html')),

    # django模板前端
    url('', include('front.urls'), name='front')

]
