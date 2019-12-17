# -*-coding:UTF-8 -*-
from rest_framework import serializers
#定义序列化类

class CommentSerializer(serializers.Serializer):
    #user表序列化器
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    workid = serializers.CharField(max_length=255)
    role = serializers.CharField(max_length=255)
    project = serializers.CharField(max_length=255)
    telephone = serializers.CharField(max_length=255)

class SlaveSerializer(serializers.Serializer):
    label = serializers.CharField(max_length=255)
    ip = serializers.CharField(max_length=255)
    bindqueue = serializers.CharField(max_length=255)
    updatetime = serializers.DateTimeField()
    status = serializers.CharField(max_length=255)

class ApiSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    project_name = serializers.CharField(max_length=255)
    module_name = serializers.CharField(max_length=255)
    api_name = serializers.CharField(max_length=255)
    protocol = serializers.CharField(max_length=255)
    header = serializers.CharField(max_length=255)
    expected = serializers.CharField(max_length=255)