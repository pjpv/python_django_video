# -*- coding: utf-8 -*-
# @Time :   2018/11/30
# @Author   :   Greendev
# @Project  : video
# @File :   serializers.py


from django.conf import settings
from rest_framework import serializers
from video.models import videoModel

from line.serializers import LineAppSerializer
from line.models import lineModel

class VideoAppSerializer(serializers.ModelSerializer):
    # line = LineSerializer()
    line = serializers.SerializerMethodField()

    def get_line(self,obj):
        l = lineModel.objects.get(id=obj.line.id)
        serlalizers =  LineAppSerializer(l, many=False)
        return serlalizers.data

    class Meta:
        model = videoModel
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = videoModel
        fields = '__all__'
