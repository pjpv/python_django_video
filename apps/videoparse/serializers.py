# -*- coding: utf-8 -*-
# @Time :   2018/11/30
# @Author   :   Greendev
# @Project  : video
# @File :   serializers.py


from rest_framework import serializers

from videoparse.models import videoParseModel


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




class VideoParseSerializer(serializers.ModelSerializer):
    class Meta:
        model = videoParseModel
        fields = '__all__'

