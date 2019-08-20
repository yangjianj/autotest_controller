# -*- coding: utf-8 -*-
from app_demo1.lib.tool import *
from app_demo2.lib.page_handler import Pagehandler
from app_demo2.lib.page_operate import Operate

class Testcase():
	def __init__(self,steps):
		self.steps = steps
		self.result = None
		self.operate = None
		self.time=0

	def run(self):
		self.setup()
		self.runstep()
		self.teardown()

	def runstep(self):
		for step in self.steps:
			if step[3] == "get":
				msg = {"action": step[3], "page": step[4], "element": step[5]}
				if step[6] != '':
					msg.update(json.loads(step[6]))
				self.operate = Operate(json.loads(step[6])['url'],browser='chrome')
				self.operate.execute(msg)
				self.operate.handler.maximize_windows(1)
			else:
				msg={"action":step[3],"page":step[4],"element":step[5]}
				if step[6] != '':
					msg.update(json.loads(step[6]))
				print(msg)
				result = self.operate.execute(msg)

	def setup(self):
		pass

	def teardown(self):
		pass

	def log(self):
		pass

	def _write_result(self):
		pass