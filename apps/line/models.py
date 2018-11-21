from django.db import models


# Create your models here.

class lineModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='名称', help_text='名称', null=False)
    subject = models.ForeignKey('subject.subjectModel', verbose_name='主题', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = verbose_name = '播放线路'

    def __str__(self):
        return '{subject}-{name}'.format(subject=self.subject.name, name=self.name)
