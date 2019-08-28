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
		self.variable={}

	def loadcases(self,excel,suitename):
		self.name = suitename
		self.casedata = import_excel_data(excel,suitename)
		self._data_split_for_suite()

	def _data_split_for_suite(self):
		_curr_case = []
		for row in self.casedata[config.EXCELMAPPING["suitebegine"]:]:
			if row[1] == "SUITE_SETUP":
				self.setup_rows.append(row)
			elif row[1] == "SUITE_TEARDOWN":
				self.teardown_rows.append(row)
			else:
				if _curr_case == []:
					_curr_case.append(row)
				elif row[config.EXCELMAPPING["用例编号"]] == '' or row[config.EXCELMAPPING["用例编号"]] == _curr_case[-1][
					config.EXCELMAPPING["用例编号"]]:
					_curr_case.append(row)
				else:
					self.testcases.append(Testcase(_curr_case[0:], self.operate))
					_curr_case.clear()
					_curr_case.append(row)
			if row is self.casedata[-1]:
				self.testcases.append(Testcase(_curr_case[0:], self.operate))

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
			result["re"]["steps"][0][config.EXCELMAPPING["执行时间"]]=str(result["spend"])
			self.spendtime = self.spendtime+result["spend"]
			self._write_result(result["re"]["steps"])
		self.teardown()

	def _update_case(self,case):
		case.operate = self.operate
		case.suite_dir = self.suite_dir
		case.suite_variable = self.variable

	def execute(self,msg):
		try:
			emeth = getattr(self, msg['action'])
			message = emeth(msg)
			re = {"result": "passed", "message": message}
		except Exception as error:
			message=self.operate.execute(msg)
			re = message
		return re

	def setup(self):
		_setup_result = []
		for i in self.casedata[0:config.EXCELMAPPING["suitebegine"]]:
			_setup_result.append(i)
		for row in self.setup_rows:
			msg = {"action": row[config.EXCELMAPPING["操作"]], "page": row[config.EXCELMAPPING["PageName"]],
			       "element": row[config.EXCELMAPPING["元素名称"]]}
			if row[config.EXCELMAPPING["value"]] != '':
				msg.update(json.loads(row[config.EXCELMAPPING["value"]]))
			result=self.execute(msg)
			_setup_result.append(self._record_result(row, result))
		self._write_result(_setup_result)

	def teardown(self):
		_teardown_result=[]
		for row in self.teardown_rows:
			msg = {"action": row[config.EXCELMAPPING["操作"]], "page": row[config.EXCELMAPPING["PageName"]],
			       "element": row[config.EXCELMAPPING["元素名称"]]}
			if row[config.EXCELMAPPING["value"]] != '':
				msg.update(json.loads(row[config.EXCELMAPPING["value"]]))
			result=self.execute(msg)
			_teardown_result.append(self._record_result(row, result))
		self._write_result(_teardown_result)

	def set_variable(self,msg):
		del msg["action"]
		del msg["page"]
		del msg["element"]
		self.variable.update(msg)

	def open_browser(self,msg):
		self.operate = Operate(msg["website"], browser=msg["browser"])
		return self.operate

	def _write_result(self,caseresult):
		export_data(caseresult,self.name,os.path.join(self.suite_dir,'test.xlsx'))

	def _record_result(self,step,result):
		step[config.EXCELMAPPING["执行结果"]] = result["result"]
		step[config.EXCELMAPPING["执行信息"]] = str(result["message"])
		return step


if __name__ == '__main__':
	te = Testsuit()
	te.loadcases(config.UI_CASE['test'],"lianjia1")
	print(te.testcases)
	for i in te.testcases:
		print(i.steps)
	te.run()