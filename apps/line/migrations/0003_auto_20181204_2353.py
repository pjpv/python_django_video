# Generated by Django 2.1.3 on 2018-12-04 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('line', '0002_auto_20181122_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='linemodel',
            name='order',
            field=models.IntegerField(default=999, help_text='排序', verbose_name='排序'),
        ),
        migrations.AlterField(
            model_name='linemodel',
            name='name',
            field=models.CharField(help_text='播放线路名称', max_length=50, verbose_name='播放线路名称'),
        ),
    ]
