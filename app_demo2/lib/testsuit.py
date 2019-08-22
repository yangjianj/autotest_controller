# -*- coding: utf-8 -*-
from app_demo2.lib.testcase import Testcase
from app_demo1.lib.tool import *
import app_demo1.config.config
from app_demo2.lib.page_operate import Operate

class Testsuit():
	#一个testsuit对应一个excel的sheet
	def __init__(self):
		self.casedata = None
		self.operate = None
		self.testcases = []
		self.name = None
		self.result=[]
		self.passed=0
		self.failed=0
		self.time=0
		self._setup_rows = []
		self._teardown_rows = []

	def loadcases(self,excel):
		self.casedata = import_excel_data(excel)

	def _data_split_for_suite(self):
		index = 0
		for row in self.casedata:
			if row[1] == "SUITE_SETUP":
				self._setup_rows.append(index)
			elif row[1] == "SUITE_TEARDOWN":
				self._teardown_rows.append(index)
			index = index+1
		_curr_case = []
		_case_setup=self._setup_rows[-1]+1
		_case_teardown=self._teardown_rows[0]-1

		#页面case部分步骤
		for step in self.casedata[_case_setup:_case_teardown]:
			if _curr_case == []:
				_curr_case.append(step)
			elif step[0] == '' or step[0] == _curr_case[-1][0]:
				_curr_case.append(step)
			else:
				self.testcases.append(Testcase(_curr_case,self.operate))
				_curr_case.clear()
				_curr_case.append(step)
			if step == self.casedata[_case_teardown]:
				self.testcases.append(Testcase(_curr_case,self.operate))

	def run(self):
		self._data_split_for_suite()
		self.setup()
		for case in self.testcases:
			result=case.run()
			self.result.append(result)
			self._write_result(result)
		self.teardown()

	def setup(self):
		for index in self._setup_rows:
			if self.casedata[index][3] == "open_browser":
				params=json.loads(self.casedata[index][6])
				self.operate = Operate(params["website"],browser=params["browser"])
			else:
				msg = {"action": self.casedata[index][3], "page": self.casedata[index][4], "element": self.casedata[index][5]}
				if self.casedata[index][6] != '':
					msg.update(json.loads(self.casedata[index][6]))
				self.operate.execute(msg)

	def teardown(self):
		for index in self._setup_rows:
			msg = {"action": self.casedata[index][3], "page": self.casedata[index][4],
			       "element": self.casedata[index][5]}
			if self.casedata[index][6] != '':
				msg.update(json.loads(self.casedata[index][6]))
			self.operate.execute(msg)

	def _write_result(self,caseresult):
		pass


if __name__ == '__main__':
	te = Testsuit()
	te.loadcases(config.UI_CASE['test'])
	te.run()