# Generated by Django 2.1.3 on 2018-12-05 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0009_auto_20181204_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectmodel',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, help_text='年代', verbose_name='年代'),
        ),
    ]
