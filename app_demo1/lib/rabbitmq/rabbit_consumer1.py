# -*- coding: utf-8 -*-
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.

channel.queue_declare(queue='hello1')  # 声明队列，保证程序不出错

def callback(ch, method, properties, body):
    print("-->ch", ch)
    print("-->method", method)
    print("-->properties", properties)
    print("[x] Received %r" % body)  # 一条消息被一个消费者接收后，该消息就从队列删除

channel.basic_consume(callback,  # 回调函数，一接收到消息就调用回调函数
                      queue='hello1',
                      no_ack=False)  # 消费完毕后向服务端发送一个确认，默认为False

print('[*] Waiting for messages.To exit press CTRL+C')
channel.start_consuming()