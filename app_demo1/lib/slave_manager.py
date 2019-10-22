# -*- coding: utf-8 -*-
import datetime
from app_demo1.models import Slave
from app_demo1.lib.database_model import SlaveSerializer

class SlaveManager():
    def __init__(self):
        pass

    def get_all_slave(self):
        all = Slave.objects.all()
        alljson = SlaveSerializer(instance=all, many=True)
        return alljson

    def enable_slave(self,ip):
        slave = Slave.objects.get(username=ip)
        slave.status = 'enable'
        slave.save()

    def disable_slave(self,ip):
        slave = Slave.objects.get(username=ip)
        slave.status = 'disable'
        slave.save()

    def change_label(self,ip,label):
        slave = Slave.objects.get(username=ip)
        slave.label = label
        slave.save()

    def update_timestamp(self,ip,updatetime):
        try:
            slave = Slave.objects.get(ip=ip)
            slave.updatetime = updatetime
            slave.save()
            return True
        except Exception as e:
            return {"message":str(e)}



