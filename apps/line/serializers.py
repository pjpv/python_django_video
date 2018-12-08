# -*- coding: utf-8 -*-
# @Time :   2018/11/30
# @Author   :   Greendev
# @Project  : video
# @File :   serializers.py


from rest_framework import serializers
from line.models import lineModel
from subject.serializers import SubjectAppSerializer

from video.models import videoModel


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = videoModel
        fields = ('id', 'name')


class LineAppSerializer(serializers.ModelSerializer):
    subject = SubjectAppSerializer()
    list = serializers.SerializerMethodField()

    def get_list(self, obj):
        # 显示播放线路下所有视频
        videos = videoModel.objects.filter(line=obj).order_by('order', 'add_time')
        serlalizers = VideoSerializer(videos, many=True)
        return serlalizers.data

    class Meta:
        model = lineModel
        fields = '__all__'


class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = lineModel
        fields = '__all__'
