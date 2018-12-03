from subject.models import subjectModel
# rest framework
from rest_framework import viewsets
from rest_framework.generics import mixins
from rest_framework.pagination import PageNumberPagination

from line.models import lineModel
from line.serializers import LineSerializer

# 过滤
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class LinePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class LineViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    列出所有的播放线路或者创建一个新的播放线路。
    """
    queryset = lineModel.objects.all().order_by('id')
    serializer_class = LineSerializer
    pagination_class = LinePagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('subject',)
    search_fields = ('name',)
