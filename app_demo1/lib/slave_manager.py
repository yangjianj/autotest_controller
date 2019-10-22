# -*- coding: utf-8 -*-
import datetime
from app_demo1.models import Slave
from app_demo1.lib.database_model import SlaveSerializer

class SlaveManager():
    def __init__(self):
        pass

    def get_all_slave(self):
        all = Slave().objects.all()
        alljson = SlaveSerializer(instance=all, many=True)
        return alljson

    def enable_slave(self,slaveip):
        slave = Slave().objects.get(username=slaveip)
        slave.status = 'enable'
        slave.save()

    def disable_slave(self,slaveip):
        slave = Slave().objects.get(username=slaveip)
        slave.status = 'disable'
        slave.save()

    def change_label(self,slaveip,label):
        slave = Slave().objects.get(username=slaveip)
        slave.label = label
        slave.save()

    def update_timestamp(self,slaveip,timestamp):
        slave = Slave().objects.get(username=slaveip)
        slave.timestamp = timestamp
        slave.save()

