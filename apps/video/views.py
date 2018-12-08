from django.shortcuts import render, reverse, render_to_response
from django.views import View
from subject.models import subjectModel
from django.shortcuts import get_object_or_404
from video.models import videoModel
from line.models import lineModel

# 事务处理
from django.db import transaction
# REST Framework
from rest_framework import viewsets
from rest_framework.generics import mixins
from rest_framework.pagination import PageNumberPagination

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import list_route, action

from video.serializers import VideoAppSerializer, VideoSerializer

# 权限
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

# 过滤
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class playView(View):
    def get(self, request, cid, subid, id):
        video = get_object_or_404(videoModel, id=id)
        subject = video.line.subject

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
        breadcrumbs.append(
            {'title': subject.name, 'url': reverse('subject', kwargs={'cid': subject.category_id, 'id': subject.id})})
        breadcrumbs.append({'title': video.name})

        template_name = 'video/play_dplayer.html'
        if video.player == 1:
            template_name = 'video/play_ckplayer.html'
        elif video.player == 2:
            template_name = 'video/iframe.html'

        response = render(request, template_name,
                          context={'video': video, 'subject': subject, 'lines': l_list, 'breadcrumbs': breadcrumbs})
        # response["Access-Control-Allow-Origin"] = "*"
        return response


class html5View(View):
    def get(self, request):
        return render(request, 'video/html5.html')


# Create your views here.

class VideoPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class VideoViewSet(mixins.ListModelMixin,      # 列表
                   mixins.RetrieveModelMixin,    # 详细
                   mixins.CreateModelMixin,      # 创建
                   mixins.UpdateModelMixin,      # 更新
                   mixins.DestroyModelMixin,     # 删除
                   viewsets.GenericViewSet):
    """
    列出所有的播放线路或者创建一个新的播放线路。
    """
    queryset = videoModel.objects.all().order_by('order', '-add_time')
    serializer_class = VideoAppSerializer
    pagination_class = VideoPagination

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('line',)
    search_fields = ('name',)
    ordering_fields = ('order', 'add_time')

    # permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        '''
        定义序列号类
        :return:
        '''
        # date_type = self.request.query_params.get('type', None)
        cient_type = self.request.META.get('HTTP_CLIENTTYPE', '')
        if cient_type.upper() in ('APP',):
            return VideoAppSerializer
        return VideoSerializer

    def get_permissions(self):
        """
        实例化并返回此视图所需的权限列表。
        Instantiates and returns the list of permissions that this view requires.
        'get': 'list', 'post': 'create'
        """
        # 获取创建每个人都有权限，其他需要管理员权限
        if self.action in ('get', 'retrieve', 'list'):
            permission_classes = [AllowAny]
            # return None
        # elif self.action == 'create':
        #     permission_classes = [IsAuthenticated]
        # elif self.http_method_names == 'options':
        #     permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    # @list_route(['put'], url_path='sort')
    @action(['put'], url_path='sort', detail=False)
    def Sort(self, request, *args, **kwargs):
        '''
        对播放列表排序，传入数据播放列表ID数组，成功返回201
        '''
        data = request.data

        if isinstance(data, list):
            try:
                with transaction.atomic():
                    for line in data:
                        for (i, id) in enumerate(line['indexs']):
                            item = videoModel.objects.filter(line__id=line['lineId'], id=id)
                            if item:
                                item[0].order = i
                                item[0].save()
            except Exception as e:
                # transaction.rollback()
                return Response('保存数据失败', status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response('上传数据错误', status=status.HTTP_401_UNAUTHORIZED)

        return Response('排序成功', status=status.HTTP_201_CREATED)
