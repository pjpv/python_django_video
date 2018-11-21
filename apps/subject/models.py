from django.db import models


# Create your models here.

class subjectModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='名称', help_text='名称', null=False)
    category = models.ForeignKey('category.categoryModel', verbose_name='分类', null=True, on_delete=models.SET_NULL)
    cover = models.URLField(verbose_name='封面链接', help_text='封面链接', default='', null=True)  # 不打算本地存储

    class Meta:
        verbose_name_plural = verbose_name = '主题'

    def __str__(self):
        return self.name
