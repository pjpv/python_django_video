# -*- coding: utf-8 -*-
# @Time :   2018/11/30
# @Author   :   Greendev
# @Project  : video
# @File :   serializers.py


from rest_framework import serializers
from video.models import videoModel
from line.serializers import LineSerializer


class VideoSerializer(serializers.ModelSerializer):
    line = LineSerializer()

    class Meta:
        model = videoModel
        fields = '__all__'
