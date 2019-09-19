# -*-coding:UTF-8 -*-
from app_demo1.models import Player
from app_demo1.models import Yang

def get_yang():
    list1 = Yang.objects.all()
    for item in list1:
        print(item.id,item.name)
    return list1.first()


if __name__ == '__main__':
    print(get_yang())