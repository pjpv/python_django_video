from django.db import models


# Create your models here.


class videoModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='视频名称', help_text='视频名称', null=False, default='全集')
    link = models.CharField(max_length=4096, verbose_name='视频地址', help_text='视频地址', null=False, default='')
    line = models.ForeignKey('line.lineModel', verbose_name='线路', on_delete=models.CASCADE)
    PLAYER_CHOICES = (
        (0, 'DPlayer'),
        (1, 'ckPlayer'),
        (2, 'iframe'),
    )
    player = models.IntegerField(choices=PLAYER_CHOICES, verbose_name='播放器', help_text='播放器', default=0)
    live = models.BooleanField(verbose_name='直播', help_text='直播', default=False)
    add_time = models.DateTimeField(verbose_name='添加时间', help_text='添加时间', auto_now_add=True)

    class Meta:
        verbose_name_plural = verbose_name = '视频'

    def __str__(self):
        return '{subject}-{line}-{name}'.format(subject=self.line.subject.name, line=self.line.name, name=self.name)
