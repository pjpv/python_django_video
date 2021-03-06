# Generated by Django 2.1.3 on 2018-11-22 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0003_subjectmodel_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjectmodel',
            name='actress',
            field=models.CharField(default='无', help_text='演员', max_length=250, verbose_name='演员'),
        ),
        migrations.AddField(
            model_name='subjectmodel',
            name='area',
            field=models.CharField(default='中国', help_text='地区', max_length=50, verbose_name='地区'),
        ),
        migrations.AddField(
            model_name='subjectmodel',
            name='director',
            field=models.CharField(default='无', help_text='导演', max_length=250, verbose_name='导演'),
        ),
        migrations.AddField(
            model_name='subjectmodel',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, help_text='年代', verbose_name='年代'),
        ),
        migrations.AddField(
            model_name='subjectmodel',
            name='update_time',
            field=models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间'),
        ),
    ]
