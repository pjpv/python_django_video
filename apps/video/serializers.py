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

from videoparse.models import videoParseModel

class VideoAppSerializer(serializers.ModelSerializer):
    # line = LineSerializer()
    line = serializers.SerializerMethodField()
    video_parse_link = serializers.SerializerMethodField()

    def get_line(self,obj):
        l = lineModel.objects.get(id=obj.line.id)
        serlalizers =  LineAppSerializer(l, many=False)
        return serlalizers.data


    def get_video_parse_link(self, obj):
        try:
            p = videoParseModel.objects.get(id=obj.video_parse_id)
            return p.parse_link
        except Exception as e:
            print(e)
            return ''

    class Meta:
        model = videoModel
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = videoModel
        fields = '__all__'
