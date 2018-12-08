from django.db import models


class videoParseModel(models.Model):
    '''
    爬虫log
    '''
    id = models.AutoField(primary_key=True)
    parse_link = models.CharField(max_length=4096, verbose_name='解析API', help_text='解析API', null=False, default='')
