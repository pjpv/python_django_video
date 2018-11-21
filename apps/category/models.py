from django.db import models


# Create your models here.
class categoryModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='分类名称', help_text='分类名称')
    order = models.IntegerField(verbose_name='排序', help_text='排序', default=999)
    inHead = models.BooleanField(verbose_name='是否顶部显示', help_text='是否顶部显示', default=True)

    class Meta:
        verbose_name_plural = verbose_name = '分类'

    def __str__(self):
        return self.name
