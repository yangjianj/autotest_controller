# -*- coding: utf-8 -*-
from app_demo2.lib.testcase import Testcase
from app_demo1.lib.tool import *
import app_demo1.config.config

class Testsuit():
	def __init__(self):
		self.casedata = None
		self.testcases = []
		self.name = None
		self.result=[]
		self.passed=0
		self.failed=0
		self.time=0

	def loadcases(self,excel):
		self.casedata = import_excel_data(excel)
		_curr_case = []
		for step in self.casedata[1:]:
			if _curr_case == []:
				_curr_case.append(step)
			elif step[0] == '' or  step[0] ==  _curr_case[-1][0]:
				_curr_case.append(step)
			else:
				self.testcases.append(Testcase(_curr_case))
				_curr_case.clear()
				_curr_case.append(step)
			if step == self.casedata[-1]:
				self.testcases.append(Testcase(_curr_case))


	def run(self):
		for case in self.testcases:
			self.result.append(case.run())

	def setup(self):
		pass

	def teardown(self):
		pass

	def _write_result(self):
		pass

if __name__ == '__main__':
	te = Testsuit()
	te.loadcases(config.UI_CASE['test'])
	te.run()