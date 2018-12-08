from subject.models import subjectModel
# 事务处理
from django.db import transaction

# rest framework
from rest_framework import viewsets
from rest_framework.generics import mixins
from rest_framework.pagination import PageNumberPagination

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import list_route, action

from line.models import lineModel
from line.serializers import LineSerializer, LineAppSerializer

# 过滤
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# 权限
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny


# Create your views here.

class LinePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class LineViewSet(mixins.ListModelMixin,  # 列表
                  mixins.RetrieveModelMixin,  # 详细
                  mixins.CreateModelMixin,  # 创建
                  mixins.UpdateModelMixin,  # 更新
                  mixins.DestroyModelMixin,  # 删除
                  viewsets.GenericViewSet):
    """
    列出所有的播放线路或者创建一个新的播放线路。
    """
    queryset = lineModel.objects.all()
    serializer_class = LineSerializer
    pagination_class = LinePagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('subject',)
    search_fields = ('name',)
    ordering_fields = ('order', 'id')

    @action(['put'], url_path='sort', detail=False)
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
                        item = lineModel.objects.filter(subject_id=subject_id, id=id)
                        if item:
                            item[0].order = i
                            item[0].save()
            except Exception as e:
                # transaction.rollback()
                return Response('保存数据失败', status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response('上传数据错误', status=status.HTTP_401_UNAUTHORIZED)

        return Response('排序成功', status=status.HTTP_201_CREATED)

    def get_permissions(self):
        """
        实例化并返回此视图所需的权限列表。
        Instantiates and returns the list of permissions that this view requires.
        'get': 'list', 'post': 'create'
        """
        # 获取创建每个人都有权限，其他需要管理员权限
        if self.action in ('get', 'list'):
            permission_classes = [AllowAny]
        # elif self.action == 'create':
        #     permission_classes = [IsAuthenticated]
        # elif self.http_method_names == 'options':
        #     permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        '''
        定义序列化类
        :return:
        '''
        type = self.request.query_params.get('type', '')
        if (type == 'simple'):
            return LineSerializer

        cient_type = self.request.META.get('HTTP_CLIENTTYPE', None)
        if cient_type and cient_type.upper() in ('APP', 'ADMIN'):
            return LineAppSerializer

        return LineSerializer
