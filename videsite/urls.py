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

# JWT
from rest_framework_jwt.views import obtain_jwt_token
# rest framework 文档
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT
    url(r'^api/api-token-auth/$', obtain_jwt_token),

    # rest_framework auth
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^docs/', include_docs_urls(title='zfdev movie')),  # rest framework 文档

    # API
    url('api/', include('api.urls'), name='api'),

    # url('^(?P<path>crossdomain.xml)$', serve, name='crossdomain'),


    # django模板前端
    url('o/', include('front.urls'), name='front'),

    # vue 前端
    url('iadmin/', TemplateView.as_view(template_name='iadmin.html')),
    # vue 前端
    url('', TemplateView.as_view(template_name='index_prod.html')),
]

if settings.ENABLE_DEBUG_TOOLBAR:
    # static and media
    # from django.conf.urls.static import static
    # from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    #
    # urlpatterns.extend(
    #     staticfiles_urlpatterns()
    #     + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # )

    # debug toolbar
    import debug_toolbar

    urlpatterns.insert(0, path("__debug__/", include(debug_toolbar.urls)))
