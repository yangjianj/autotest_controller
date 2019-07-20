# -*- coding: utf-8 -*-
#from __future__ import absolute_import, unicode_literals  #相对路径转为绝对路径
from celery import Celery

#python 3.6 ;celery 4.4.0.rc2 ; redis 3.2.1
#初始化celery实例时加载配置，broker:任务队列的中间人；backend:任务执行结果的存储
app = Celery("task1",
             broker="redis://127.0.0.1:6379/0",
             backend="redis://127.0.0.1:6379/0",
             include=['task1'])

@app.task    #装饰器，将函数装饰为Task实例    使用默认queue
def add(x,y):
    return x+y

if __name__ == '__main__':
    #app.start  #consumer运行
    for i in range(10):
        add.delay(i,200)   #producer发布任务到redis

'''
操作步骤：
1.启动redis
2.启动worker:celery -A task1 worker --loglevel=info -P eventlet
3.发布任务：运行此脚本
'''