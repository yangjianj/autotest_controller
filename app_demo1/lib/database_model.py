# -*-coding:UTF-8 -*-
from app_demo1.models import Player,Yang,User
from app_demo1.lib.app_serializers import CommentSerializer

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