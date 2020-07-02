# -*- coding: utf-8 -*-
from datetime import datetime
import  pika,time,random
from app_demo1.lib.redisConnector import Connector as redisConnector
from app_demo1.config import config as CONFIG

'''
对已创建任务未执行任务进行切片环境匹配检查，有空闲且匹配的环境则发送给对应worker的消息通道
'''

def send_task(self,task,slave):
    #发送task到redis
    task = {
        "id": "taskid123456",
        "name": "name123",
        "slave": "slave1",
        "version": "version001",
        "project": "pro1",
        "cases": ["suite1", "suite111", "suite2", "suite211", "suite3", "suite311", "suite411", "suite4"]
    }
    redis = redisConnector()
    redis.publish(CONFIG.TASK_TOPIC,task)


def send_task1(self, task, slave):
    # 发送任务给空闲slave
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()  # 生成管道，在管道里跑不同的队列
    
    # 声明queue
    channel.queue_declare(queue='hello1')
    
    slave_task = self.build_task()
    channel.basic_publish(exchange='',  # 先把数据发给exchange交换器,exchage再发给相应队列
                          routing_key='hello1',  # 向"hello1'队列发数据
                          body=str(slave_task)  # 发的消息
                          )
    connection.close()


if __name__ == '__main__':
    while(1):
        #循环查询任务数据库中未
        time.sleep(2)