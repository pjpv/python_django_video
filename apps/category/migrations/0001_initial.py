# Generated by Django 2.1.3 on 2018-11-21 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoryModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='分类名称', max_length=50, verbose_name='分类名称')),
                ('order', models.IntegerField(default=999, help_text='排序', verbose_name='排序')),
                ('inHead', models.BooleanField(default=True, help_text='是否顶部显示', verbose_name='是否顶部显示')),
            ],
        ),
    ]