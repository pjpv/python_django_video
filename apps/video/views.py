from django.shortcuts import render, reverse,render_to_response
from django.views import View
from subject.models import subjectModel
from django.shortcuts import get_object_or_404
from video.models import videoModel
from line.models import lineModel

# REST Framework
from rest_framework import viewsets
from rest_framework.generics import mixins
from rest_framework.pagination import PageNumberPagination

from video.serializers import VideoSerializer


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

class LinePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100



class VideoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    """
    列出所有的播放线路或者创建一个新的播放线路。
    """
    queryset = videoModel.objects.all().order_by('add_time')
    serializer_class = VideoSerializer
    pagination_class = LinePagination