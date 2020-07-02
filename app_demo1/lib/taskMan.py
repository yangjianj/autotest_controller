# -*- coding: utf-8 -*-
from datetime import datetime
import  time,random
from app_demo1.lib.redisConnector import Connector as redisConnector
from app_demo1.models import task_case_mapping
from app_demo1.lib.database_con import DataManager
from app_demo1.models import UiTaskCaseTable

class TaskManager():
	def __init__(self,type):
		# type : ui , api
		timestramp = datetime.now().strftime( '%Y-%m-%d_%H-%M-%S' )
		self.id = type+timestramp
		self.redis = redisConnector()
		self.db = DataManager()
	
	def create_task(self,version,product,caseid_list):
		pass
	
	def delete_task(self):
		pass
	
	def serach_task(self):
		pass

	def create_task(self,type,data):
		#创建任务，并存储到任务数据库
		version = data["version"]
		timestamp = time.strftime('%Y%m%d%H%M%S')
		taskid = type+'_'+timestamp+str(random.randrange(0, 101, 2))
		task = {
			"taskid":taskid,
			"type":type,
			"version":version,
			"data":data
		}
		
		self.db.create_ui_task(task)
		return True

	def add_cases_to_task(self,taskid,caselist):
		#添加caseid到任务表中
		for item in caselist:
			obj = {'taskid': taskid, 'caseid': item['caseid'],'status':'wait'}
			UiTaskCaseTable.objects.create(obj)
		
	def update_task(self,task_list):
		#任务完成更新任务状态
		pass


if __name__ == '__main__':
	tm= TaskManager()
	

