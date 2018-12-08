from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views import View
from rest_framework.decorators import action
from rest_framework import viewsets
# rest framework
from rest_framework.generics import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status

from spider.models import spiderModel
from spider.serializers import SpiderSerializer

from category.models import categoryModel
from subject.models import subjectModel

# 事务处理
from django.db import transaction
# 过滤
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class SpiderPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class SpiderViewSet(mixins.ListModelMixin,  # 列表
                    mixins.RetrieveModelMixin,  # 详细
                    mixins.CreateModelMixin,  # 创建
                    mixins.UpdateModelMixin,  # 更新
                    mixins.DestroyModelMixin,  # 删除
                    viewsets.GenericViewSet):
    """
    列出所有的主题或者创建一个新的主题。
    """
    queryset = spiderModel.objects.all()
    serializer_class = SpiderSerializer
    pagination_class = SpiderPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('owner','spider_type',)
    search_fields = ('name', 'project')
    ordering_fields = ('order', 'owner', 'link')

    # def get_serializer_class(self):
    #     '''
    #     定义序列化类
    #     :return:
    #     '''
    #     cient_type = self.request.META.get('HTTP_CLIENTTYPE', '')
    #     if cient_type.upper() == 'APP' or self.request.query_params.get('CLIENTTYPE', '').upper() == 'APP':
    #         return CategoryAppSerializer
    #     return CategorySerializer

    @action(['patch'], url_path='sort', detail=False)
    def Sort(self, request, *args, **kwargs):
        '''
        对播放列表排序，传入数据播放列表ID数组，成功返回201
        '''
        subject_id = request.data.get('sid')
        indexs = request.data.get('indexs')
        if indexs:
            try:
                with transaction.atomic():
                    for (i, id) in enumerate(indexs):
                        item = spiderModel.objects.filter(owner=subject_id, id=id)
                        if item:
                            item[0].order = i
                            item[0].save()
            except Exception as e:
                # transaction.rollback()
                return Response('保存数据失败', status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response('上传数据错误', status=status.HTTP_401_UNAUTHORIZED)

        return Response('排序成功', status=status.HTTP_201_CREATED)
