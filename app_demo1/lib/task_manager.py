# -*- coding: utf-8 -*-
import  pika,time
class TaskManager():
	def __init__(self):
		pass

	def send_task(self,task,slave):
		connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
		channel = connection.channel()  # 生成管道，在管道里跑不同的队列

		# 声明queue
		channel.queue_declare(queue='hello1')

		slave_task = self.build_task()
		channel.basic_publish(exchange='',  # 先把数据发给exchange交换器,exchage再发给相应队列
							  routing_key='hello1',  # 向"hello1'队列发数据
							  body=str(slave_task) # 发的消息
							  )
		connection.close()

	def build_task(self):
		#{"tasktype":"ui","message":""}
		slave_task = {"tasktype":"ui","message":""}
		return slave_task

	def update_task(self,task_list):
		pass


