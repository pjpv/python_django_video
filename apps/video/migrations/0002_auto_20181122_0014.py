# Generated by Django 2.1.3 on 2018-11-21 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='videomodel',
            options={'verbose_name': '视频', 'verbose_name_plural': '视频'},
        ),
        migrations.RenameField(
            model_name='videomodel',
            old_name='视频地址',
            new_name='link',
        ),
    ]
