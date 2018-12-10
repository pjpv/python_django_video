from django.db import models
import datetime
from video.models import videoModel
from line.models import lineModel


# Create your models here.

class subjectModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='主题名称', help_text='主题名称', null=False)
    category = models.ForeignKey('category.categoryModel', verbose_name='分类', null=True, on_delete=models.SET_NULL)
    cover = models.URLField(verbose_name='封面链接', help_text='封面链接', default='', null=True)  # 不打算本地存储
    STATE_CHOICES = (
        (0, '热播中'),
        (1, '全集'),
    )
    state = models.IntegerField(choices=STATE_CHOICES, verbose_name='状态', help_text='状态', default=0)
    pub_date = models.DateTimeField(verbose_name='年代', help_text='年代', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', help_text='更新时间', auto_now=True)
    area = models.CharField(max_length=50, verbose_name='地区', help_text='地区', default='中国')
    director = models.CharField(max_length=250, verbose_name='导演', help_text='导演', default='无')
    actress = models.CharField(max_length=1024, verbose_name='演员', help_text='演员', default='无')
    tags = models.CharField(max_length=250, verbose_name='标签', help_text='标签', default='无')
    desc = models.CharField(max_length=500, verbose_name='描述', help_text='描述', default='无')
    tips = models.CharField(max_length=30, verbose_name='提示', help_text='提示', default='')
    douban_id = models.BigIntegerField(verbose_name='豆瓣ID', help_text='豆瓣ID', default=0)

    class Meta:
        verbose_name_plural = verbose_name = '主题'

    def __str__(self):
        return self.name

    def last_video(self):
        if not hasattr(self, '_last_video_name'):
            self._last_video = self.get_last_video()
        return self._last_video

    def get_last_video(self):
        """
        返回最后添加的视频名称
        """

        video = videoModel.objects.filter(line__subject=self).order_by('-add_time')
        if video:
            return video[0]
        else:
            return None
