# -*- coding: utf-8 -*-
import pika

class RabbitConsumer:
    def __init__(self,queuex,server):
        self.queue=queuex
        self.server=server
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(server))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queuex)  # 声明队列，保证程序不出错

    def run(self):
        self.channel.basic_consume(self.call_back,  # 回调函数，一接收到消息就调用回调函数
                              queue=self.queue,
                              no_ack=False)
        self.channel.start_consuming()

    def call_back(self,ch, method, properties, body):
        try:
            func= getattr(self,body['action'],None)
            if func:
                return func(body['params'])
            else:
                return "no active"
        except Exception as e:
            print(e)
        finally:
            pass
    def task_manage(self,task):
        pass

    def get_data(self):
        return 1

    def post_data(self):
        return 1


if __name__ == '__main__':
    demo=RabbitConsumer("queue1",'localhost')
    demo.run()