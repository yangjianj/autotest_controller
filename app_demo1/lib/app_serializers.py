# -*-coding:UTF-8 -*-
from rest_framework import serializers
from app_demo1.models import Api_testcase
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
    #指定序列化字段
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    project_name = serializers.CharField(max_length=255)
    module_name = serializers.CharField(max_length=255)
    api_name = serializers.CharField(max_length=255)
    protocol = serializers.CharField(max_length=255)
    header = serializers.CharField(max_length=255)
    expected = serializers.CharField(max_length=255)
    api_link = serializers.CharField(max_length=255)
    request_data = serializers.CharField(max_length=255)
    
    def create(self, validated_data):
        #反序列化时创建一个model实例
        return Api_testcase.objects.create(**validated_data)

    def update(self, instance, validated_data):
        #反序列时更新一个model对象
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.project_name = validated_data.get('project_name', instance.project_name)
        instance.module_name = validated_data.get('module_name', instance.module_name)
        instance.api_name = validated_data.get('api_name', instance.api_name)
        instance.protocol = validated_data.get('protocol', instance.protocol)
        instance.header = validated_data.get('header', instance.header)
        instance.expected = validated_data.get('expected', instance.expected)
        instance.api_link = validated_data.get('api_link', instance.api_link)
        instance.request_data = validated_data.get('request_data', instance.request_data)
        instance.save()  #存到数据库
        return instance