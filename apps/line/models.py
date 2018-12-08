from django.db import models


# Create your models here.

class lineModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='播放线路名称', help_text='播放线路名称', null=False)
    subject = models.ForeignKey('subject.subjectModel', verbose_name='主题', on_delete=models.CASCADE)
    order = models.IntegerField(default=999, verbose_name='排序', help_text='排序')
    internal_name = models.CharField(max_length=50, verbose_name='内部名称', help_text='内部名称',
                                     null=False, default=None,blank=False, unique=True)

    class Meta:
        verbose_name_plural = verbose_name = '播放线路'

    def __str__(self):
        return self.name
