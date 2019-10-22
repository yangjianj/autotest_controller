# -*-coding:UTF-8 -*-
from rest_framework import serializers
from app_demo1.models import Player,Yang,User

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


def get_yang():
    list1 = Yang.objects.all()
    for item in list1:
        print(item.id,item.name)
    return list1.first()

def get_all_user():
    users = User.objects.all()
    user_s = CommentSerializer(instance=users,many=True)
    data = user_s.data
    return data




if __name__ == '__main__':
    print(get_yang())