from django.shortcuts import render, reverse
from django.views import View
from subject.models import subjectModel
from django.shortcuts import get_object_or_404
from video.models import videoModel
from line.models import lineModel
# rest framework
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, mixins
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from subject.serializers import SubjectSerializer
from rest_framework.pagination import PageNumberPagination

# 过滤
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class subjectView(GenericAPIView):
    def get(self, request, cid, id):
        subject = get_object_or_404(subjectModel, id=id)
        lines = lineModel.objects.filter(subject=subject)
        l_list = []
        for line in lines:
            l_list.append({
                'name': line.name,
                'videos': videoModel.objects.filter(line=line)
            })

        breadcrumbs = []
        breadcrumbs.append(
            {'title': subject.category.name, 'url': reverse('category', kwargs={'id': subject.category_id})})
        breadcrumbs.append({'title': subject.name})

        return render(request, 'subject/subject.html',
                      context={'subject': subject, 'lines': l_list, 'breadcrumbs': breadcrumbs})

        # class SubjectListView(viewsets.ViewSet):
        #     """
        #     列出所有的主题或者创建一个新的主题。
        #     """
        # def get(self, request, format=None):
        #     subjects = subjectModel.objects.all()
        #     # pagination_class = LargeResultsSetPagination
        #     serializer = SubjectSerializer(subjects, many=True)
        #     return Response(serializer.data)


class SubjectPagination(PageNumberPagination):
    page_size = 24
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class SubjectViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    """
    列出所有的主题或者创建一个新的主题。
    """
    queryset = subjectModel.objects.all()
    serializer_class = SubjectSerializer
    pagination_class = SubjectPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('category', 'state', 'pub_date', 'area', 'director', 'actress')
    search_fields = ('name', 'tags')
    ordering_fields = ('pub_date', 'update_time')
