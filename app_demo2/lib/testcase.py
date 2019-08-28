# -*- coding: utf-8 -*-
from app_demo1.lib.tool import *
import app_demo1.config.config

class Testcase():
	def __init__(self,steps,operate):
		self.steps = steps
		self.id = steps[0][config.EXCELMAPPING["用例编号"]]
		self.result = {"result":"passed","steps":[]}
		self.operate = operate
		self.suite_dir = ''
		self.case_dir = ''
		self.variable={}   #case变量存放，优先级大于suite变量
		self.suite_variable={} #suite变量存放地

	@record_time
	def run(self):
		self.case_dir =create_case_dir(self.suite_dir,self.id)
		self.setup()
		self.runstep()
		self.teardown()
		return self.result

	def runstep(self):
		for step in self.steps:
			if self.result["result"] == "failed" :
				block_result = {"result":"block","message":None}
				self._record_step_result(step,block_result)
				continue
			msg={"action":step[config.EXCELMAPPING["操作"]],"page":step[config.EXCELMAPPING["PageName"]],"element":step[config.EXCELMAPPING["元素名称"]]}
			if step[config.EXCELMAPPING["value"]] != '':
				msg.update(json.loads(step[config.EXCELMAPPING["value"]]))
			result = self.execute(msg)
			self._record_step_result(step,result)

	def execute(self,msg):
		#执行方法在不属于case实例方法则使用operate执行
		print(msg)
		try:
			emeth = getattr(self, msg['action'])
			message = emeth(msg)
			re = {"result": "passed", "message": message}
		except Exception as error:
			message=self.operate.execute(msg)
			re = message
		return re

	def setup(self):
		pass

	def teardown(self):
		msg = {}
		msg["filepath"] =os.path.join(self.case_dir,"ending_screen.png")
		self.operate.handler.get_screenshot_as_file(msg)

	def log(self):
		pass

	def _record_step_result(self,step,result):
		step[config.EXCELMAPPING["执行结果"]] = result["result"]
		step[config.EXCELMAPPING["执行信息"]] = str(result["message"])
		if result["result"] == "failed":
			self._error_handler(step[config.EXCELMAPPING["PageName"]])
			self.result["result"] = "failed"
		self.result["steps"].append(step)


	def _error_handler(self,curr_action):
		timestr = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
		msg = {}
		msg["filepath"] = os.path.join(self.case_dir,curr_action+timestr+".png")
		self.operate.handler.get_screenshot_as_file(msg)