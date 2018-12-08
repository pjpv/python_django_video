# -*- coding: utf-8 -*-
# @Time :   2018/11/30
# @Author   :   Greendev
# @Project  : video
# @File :   serializers.py


from rest_framework import serializers
from category.models import categoryModel
from subject.models import subjectModel


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


class SubjectNoCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = subjectModel
        fields = '__all__'


class CategoryAppSerializer(serializers.ModelSerializer):
    list = serializers.SerializerMethodField()

    def get_list(self, obj):
        # 显示6个最近更新的主题
        subjects = subjectModel.objects.filter(category=obj).order_by('-update_time')[:6]
        serlalizers = SubjectNoCategorySerializer(subjects, many=True)
        return serlalizers.data

    class Meta:
        model = categoryModel
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = categoryModel
        fields = '__all__'
