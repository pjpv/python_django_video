# -*- coding: utf-8 -*-
# @Time :   2018/11/30
# @Author   :   Greendev
# @Project  : video
# @File :   serializers.py


from django.conf import settings

from rest_framework import serializers
from subject.models import subjectModel
from category.serializers import CategoryAppSerializer,CategorySerializer


# class CategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True, help_text='ID', label='ID')
#     name = serializers.CharField(required=True, max_length=50, allow_blank=False, help_text='分类名称', label='分类名称')
#     order = serializers.IntegerField(default=999, help_text='排序', label='排序')
#     inHead = serializers.BooleanField(default=True, help_text='是否顶部显示', label='是否顶部显示')
#
#     def create(self, validated_data):
#         '''
#         创建一个新的分类
#         '''
#         return categoryModel.objects.create(**validated_data)



class SubjectAppSerializer(serializers.ModelSerializer):
    '''
    主题 序列化，用于前端展示
    '''
    category = CategorySerializer()

    class Meta:
        model = subjectModel
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    '''
    主题 序列化，用于后端数据
    '''
    pub_date = serializers.DateTimeField(format=settings.DATETIME_FORMAT)
    update_time = serializers.DateTimeField(format=settings.DATETIME_FORMAT)
    category_name = serializers.SerializerMethodField()

    def get_category_name(self, obj):
        if obj.category:
            return obj.category.name
        return ''

    class Meta:
        model = subjectModel
        fields = '__all__'
