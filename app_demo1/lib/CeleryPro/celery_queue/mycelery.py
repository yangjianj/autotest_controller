# -*- coding: utf-8 -*-
#python 3.6 ;celery 4.4.0.rc2 ; redis 3.2.1
from celery import Celery
from settings import *
import func1

app = Celery("mycelery",
             broker=c_broker,
             backend=c_backend)
             #include=['mytask'])

app.conf.update(CELERY_QUEUES=CELERY_QUEUES, CELERY_ROUTES=CELERY_ROUTES)
@app.task
def test_queue_1():
    return 'queue1'

@app.task
def test_queue_2():
    func1.meth1()
    return 'queue2'

@app.task
def no_queue():
    return 'no queue test'

if __name__ == '__main__':
    #app.start(argv=['celery', 'worker', '-l', 'info', '-f', 'logs/celery.log'])  #consumer运行
    for i in range(3):
        re=test_queue_2.delay()   #producer发布任务到redis
        print(re.get())  # 获取任务的返回结果
        print(re.successful())  # 判断任务是否成功执行

'''
操作步骤：
1.开启redis作为broker
2.不同worker分配到不同队列：
celery -A mycelery worker -l info -Q app_q1 -P eventlet
celery -A mycelery worker -l info -Q app_q2 -P eventlet
3.执行此脚本发布任务

# 此时调用main.py中的test_queue_1和test_queue_2，会发现task被分发到各个对应的celery worker服务。
# 对于没有被队列接收的sayhi函数，通过sayhi.apply_async(queue='queue_1’)可以将任务分发到queue_1

'''