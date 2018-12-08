from django.db import models


# Create your models here.
class spiderModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='爬虫名称', help_text='爬虫名称')
    order = models.IntegerField(verbose_name='排序', help_text='排序', default=999)
    type_choices = (
        (0, '主题'),
        (1, '播放列表'),
    )
    spider_type = models.IntegerField(choices=type_choices, verbose_name='爬虫类型', help_text='主题或播放列表')
    owner = models.IntegerField(verbose_name='拥有者ID', help_text='分类ID或主题ID', db_index=True)
    link = models.TextField(verbose_name='起始链接', help_text='爬虫开始的链接')
    project = models.CharField(max_length=50, verbose_name='爬虫项目名称', help_text='爬虫项目名称')
    enable = models.BooleanField(verbose_name='是否启用', help_text='是否启用', default=True)

    class Meta:
        verbose_name_plural = verbose_name = '爬虫'

    def __str__(self):
        return self.name


class spiderLogModel(models.Model):
    '''
    爬虫log
    '''
    id = models.AutoField(primary_key=True)
    spider_id = models.ForeignKey(spiderModel, on_delete=models.CASCADE)
    log = models.TextField(verbose_name='信息', default='空')
    log_type_choices = (
        (0, 'Info'),
        (1, 'Warnings'),
        (2, 'Errors'),
    )
    log_type = models.IntegerField(choices=log_type_choices, verbose_name='日志类型')
    time = models.DateTimeField(auto_now=True, verbose_name='发生时间')
