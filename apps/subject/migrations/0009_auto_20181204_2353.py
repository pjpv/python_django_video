# Generated by Django 2.1.3 on 2018-12-04 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0008_auto_20181128_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectmodel',
            name='name',
            field=models.CharField(help_text='主题名称', max_length=50, verbose_name='主题名称'),
        ),
    ]
