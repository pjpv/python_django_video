from django.db import models


# Create your models here.


class videoModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='视频名称', help_text='视频名称', null=False, default='全集')
    link = models.URLField(verbose_name='视频地址', help_text='视频地址', null=False, default='')
    line = models.ForeignKey('line.lineModel', verbose_name='线路', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = verbose_name = '视频'

    def __str__(self):
        return '{line}-{name}'.format(line=self.line.name, name=self.name)
