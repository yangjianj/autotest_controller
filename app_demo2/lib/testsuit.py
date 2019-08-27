# -*- coding: utf-8 -*-
import os,sys
import time,datetime
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
		self.spendtime=datetime.datetime.now()-datetime.datetime.now()
		self.setup_rows = []
		self.teardown_rows = []
		self.suite_dir=''

	def loadcases(self,excel,suitename):
		self.name = suitename
		self.casedata = import_excel_data(excel,suitename)
		self._data_split_for_suite()

	def _data_split_for_suite(self):
		_index = 0
		_case_start_row=[]
		_case_end_row=[]
		for row in self.casedata:
			if row[1] == "SUITE_SETUP":
				self.setup_rows.append(row)
				_case_start_row.append(_index)
			elif row[1] == "SUITE_TEARDOWN":
				self.teardown_rows.append(row)
				_case_end_row.append(_index)
			_index = _index+1
		_curr_case = []
		#页面case部分步骤
		for step in self.casedata[_case_start_row[-1]+1:_case_end_row[0]]:
			print(step)
			if _curr_case == []:
				_curr_case.append(step)
			elif step[0] == '' or step[0] == _curr_case[-1][0]:
				_curr_case.append(step)
			else:
				self.testcases.append(Testcase(_curr_case[0:],self.operate))
				_curr_case.clear()
				_curr_case.append(step)
			if step is self.casedata[_case_end_row[0]-1]:
				self.testcases.append(Testcase(_curr_case[0:],self.operate))

	def run(self):
		self.suite_dir=create_suite_dir("uitest",self.name)
		self.setup()
		for case in self.testcases:
			self._update_case(case)
			result=case.run()
			if result["re"]["result"] == "passed":
				self.passed += 1
			else:
				self.failed += 1
			self.result.append(result)
			result["re"]["steps"][0][10]=str(result["spend"])
			self.spendtime = self.spendtime+result["spend"]
			self._write_result(result["re"]["steps"])
		self.teardown()

	def _update_case(self,case):
		case.operate = self.operate
		case.suite_dir = self.suite_dir

	def setup(self):
		_setup_result = []
		for row in self.setup_rows:
			if row[4] == "open_browser":
				params=json.loads(row[7])
				self.operate = Operate(params["website"],browser=params["browser"])
				_setup_result.append(self.casedata[0])
				_setup_result.append(row)
			else:
				msg = {"action": row[4], "page": row[5], "element": row[6]}
				if row[7] != '':
					msg.update(json.loads(row[7]))
				result =self.operate.execute(msg)
				_setup_result.append(self._record_result(row,result))
		self._write_result(_setup_result)

	def teardown(self):
		_teardown_result=[]
		for row in self.teardown_rows:
			msg = {"action": row[4], "page": row[5],
			       "element": row[6]}
			if row[7] != '':
				msg.update(json.loads(row[7]))
			result=self.operate.execute(msg)
			_teardown_result.append(self._record_result(row, result))
		self._write_result(_teardown_result)

	def _write_result(self,caseresult):
		export_data(caseresult,self.name,os.path.join(self.suite_dir,'test.xlsx'))

	def _record_result(self,step,result):
		step[8] = result["result"]
		step[9] = str(result["message"])
		return step


if __name__ == '__main__':
	te = Testsuit()
	te.loadcases(config.UI_CASE['test'],"lianjia1")
	te.run()