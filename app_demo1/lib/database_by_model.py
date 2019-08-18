# -*-coding:UTF-8 -*-
from app_demo1.models import Player

def get_player():
    return Player.objects.all()

