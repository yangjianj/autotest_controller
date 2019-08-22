# -*- coding: utf-8 -*-
from app_demo1.lib.tool import *
from app_demo2.lib.page_handler import Pagehandler
from app_demo2.lib.page_operate import Operate

class Testcase():
	def __init__(self,steps,operate):
		self.steps = steps
		self.result = None
		self.operate = operate
		self.time=0

	def run(self):
		self.setup()
		self.runstep()
		self.teardown()

	def runstep(self):
		for step in self.steps:
			msg={"action":step[3],"page":step[4],"element":step[5]}
			if step[6] != '':
				msg.update(json.loads(step[6]))
			result = self.operate.execute(msg)

	def setup(self):
		pass

	def teardown(self):
		pass

	def log(self):
		pass

	def _write_result(self):
		pass