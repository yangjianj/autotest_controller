# -*- coding: utf-8 -*-
from datetime import datetime
import  pika,time,random
from app_demo1.lib.redisConnector import Connector as redisConnector

class TaskManager():
	def __init__(self,type):
		# type : ui , api
		timestramp = datetime.now().strftime( '%Y-%m-%d_%H-%M-%S' )
		self.id = type+timestramp
		self.redis = redisConnector()
	
	def create_task(self,version,product,caseid_list):
		pass
	
	def delete_task(self):
		pass
	
	def serach_task(self):
		pass

	def send_task1(self,task,slave):
		#发送任务给空闲slave
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

	def send_task(self,task,slave):
		#发送task到redis
		'''
		task = {
        "id": "taskid123456",
        "name": "name123",
        "slave": "slave1",
        "version": "version001",
        "project": "pro1",
        "cases": ["suite1", "suite111", "suite2", "suite211", "suite3", "suite311", "suite411", "suite4"]
        }
		'''
		self.redis.push()
    
	def build_task(self,type,data):
		#创建任务，并存储到任务数据库
		version = data["version"]
		caseid_list = data["caseid_list"]


		timestamp = time.strftime('%Y%m%d%H%M%S')
		taskid = type+'_'+timestamp+str(random.randrange(0, 101, 2))
		task = {
			"taskid":taskid,
			"type":type,
			"version":version,
			"data":data
		}
		return task

	def update_task(self,task_list):
		#任务完成更新任务状态
		pass
if __name__ == '__main__':
	tm= TaskManager()
	

