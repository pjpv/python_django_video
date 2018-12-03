# -*- coding: utf-8 -*-
# @Time :   2018/11/30
# @Author   :   Greendev
# @Project  : video
# @File :   serializers.py


from rest_framework import serializers
from line.models import lineModel
from subject.serializers import SubjectSerializer

from video.models import videoModel


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = videoModel
        fields = ('id', 'name')


class LineSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    list = serializers.SerializerMethodField()

    def get_list(self, obj):
        # 显示播放线路下所有视频
        videos = videoModel.objects.filter(line=obj).order_by('add_time', 'name')
        serlalizers = VideoSerializer(videos, many=True)
        return serlalizers.data

    class Meta:
        model = lineModel
        fields = '__all__'
