# Generated by Django 2.1.3 on 2018-12-06 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='spiderModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='爬虫名称', max_length=50, verbose_name='爬虫名称')),
                ('order', models.IntegerField(default=999, help_text='排序', verbose_name='排序')),
                ('spider_type', models.IntegerField(choices=[(0, '主题'), (1, '播放列表')], help_text='主题或播放列表', verbose_name='爬虫类型')),
                ('owner', models.IntegerField(help_text='分类ID或主题ID', verbose_name='拥有者ID')),
                ('link', models.TextField(help_text='爬虫开始的链接', verbose_name='起始链接')),
                ('project', models.CharField(help_text='爬虫项目名称', max_length=50, verbose_name='爬虫项目名称')),
                ('enable', models.BooleanField(default=True, help_text='是否启用', verbose_name='是否启用')),
            ],
            options={
                'verbose_name': '爬虫',
                'verbose_name_plural': '爬虫',
            },
        ),
    ]
