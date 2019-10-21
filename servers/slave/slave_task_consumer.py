# -*- coding: utf-8 -*-
import pika
from lib.task_exector import Exector
import config

con = pika.ConnectionParameters(config.masterip)
connection = pika.BlockingConnection(con)
channel = connection.channel()
channel.queue_declare(queue=config.taskqueue)  # 声明队列，保证程序不出错
def callback(ch, method, properties, body):
    print("-->ch", ch)
    print("-->method", method)
    print("-->properties", properties)
    print("[x] Received %r" % body)  # 一条消息被一个消费者接收后，该消息就从队列删除

    Exector().task_handler(body)  #处理任务

channel.basic_consume(config.taskqueue,
                      callback)

print('[*] Waiting for messages.To exit press CTRL+C')
channel.start_consuming()